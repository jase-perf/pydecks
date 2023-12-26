from bs4 import BeautifulSoup
import requests


IMPORTS_STRING = """from typing import List, Any, Optional
import datetime

from .models import _BaseModel
from .enums import _PrintableEnum
"""
CODECKS_API_REFERENCE_URL = "https://manual.codecks.io/api-reference/"
api_reference_html = requests.get(CODECKS_API_REFERENCE_URL).text
soup = BeautifulSoup(api_reference_html, "html.parser")


def get_type(type_name: str):
    if "[]" in type_name:
        return f"List[{get_type(type_name.replace('[]', ''))}]"
    if type_name == "array":
        return "list"
    if type_name in {"bigint", "int", "number"}:
        return "int"
    if type_name in {"boolean", "bool"}:
        return "bool"
    if type_name in {"date", "day"}:
        return "datetime.datetime"
    if type_name in {"string", "json"}:
        return "str"
    if type_name == "unknown":
        return "Any"
    return f'"{type_name[0].upper() + type_name[1:]}"'


def create_classes_string() -> str:
    result = ""
    sections = soup.find_all("section")
    for section in sections:
        this_section = "\n\n"
        section_id = section["id"].replace("_", "")
        subsections = section.findChildren("div", recursive=False)
        this_section += f"class {section_id[0].upper()}{section_id[1:]}(_BaseModel):\n"
        first_part = ""
        second_part = ""
        for subsection in subsections:
            subsection_title = subsection.find("h3").text
            first_part += f"    class {subsection_title}(_PrintableEnum):\n"
            contents = subsection.findChildren("div", recursive=False)[0].findChildren(
                "div", recursive=False
            )
            for content in contents:
                name, value = content.children
                isList = "[]" in value.text
                rel_type = get_type(value.text.replace("[]", "")).replace('"', "")
                first_part += f'''        class {name.text}:
            """
            Type: {rel_type}{"[]" if isList else ""}
            """

            value = "{name.text}"

'''
                second_part += f"    {name.text}: {get_type(value.text)}\n"
        this_section += first_part + second_part
        this_section += "\n    def __init__(self, id: str, data: Optional[dict]):\n"
        this_section += "        super().__init__(id, data)\n"
        result += this_section
    return result


def list_all_types() -> str:
    sections = soup.find_all("section")
    all_types = set()
    for section in sections:
        subsections = section.findChildren("div", recursive=False)
        for subsection in subsections:
            contents = subsection.findChildren("div", recursive=False)[0].findChildren(
                "div", recursive=False
            )
            for content in contents:
                _, value = content.children
                text_value = value.text.replace("[]", "")
                all_types.add(text_value)
    print("\n".join(sorted(all_types)))
    all_types


def main():
    classes_string = create_classes_string()
    print(IMPORTS_STRING + classes_string)


if __name__ == "__main__":
    main()
