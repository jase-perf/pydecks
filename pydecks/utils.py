import uuid
from typing import Union
import os
import base64
import io
import mimetypes
import base64

import requests


class Sequence:
    def __init__(self, card_sequence: Union[str, int]):
        self.letters = "123456789acefghijkoqrsuvwxyz"
        self.start_val = 28 * 29 - 1
        self.implicit_zero = True
        self.letter_to_index = {
            letter: index for index, letter in enumerate(self.letters)
        }
        self.length = len(self.letters)

        if isinstance(card_sequence, str):
            self.string = self.id = card_sequence
            self.int = self.sequence = self._seq_to_int(card_sequence)
        elif isinstance(card_sequence, int):
            self.int = self.sequence = card_sequence
            self.string = self.id = self._int_to_seq(card_sequence)

    def _int_to_seq(self, int_val):
        seq = []
        q = int_val + self.start_val
        if self.implicit_zero:
            q += 1

        while q:
            if self.implicit_zero:
                q -= 1
            r = q % self.length
            q = q // self.length
            seq.insert(0, self.letters[r])

        return "".join(seq)

    def _seq_to_int(self, seq):
        int_val = self.letter_to_index.get(seq[0], 0)
        for char in seq[1:]:
            if self.implicit_zero:
                int_val += 1
            int_val = int_val * self.length + self.letter_to_index[char]
        return int_val - self.start_val

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"Sequence(accountSeq: {self.int} id: '${self.string}')"


def add_file_to_card(file_source, card_id, user_id, subdomain):
    filename = os.path.basename(file_source)
    file_size = os.path.getsize(file_source)
    with open(file_source, "rb") as file_data:
        return process_file_upload(
            file_data, filename, file_size, card_id, user_id, subdomain
        )


def add_base64_to_card(b64_string, card_id, user_id, subdomain, filename):
    # Decode the base64 string
    image_data = base64.b64decode(b64_string)
    display(Image(image_data))
    file_like_object = io.BytesIO(image_data)

    # Call your function with the file-like object
    file_size = len(file_like_object.getvalue())
    return process_file_upload(
        file_like_object, filename, file_size, card_id, user_id, subdomain
    )


def process_file_upload(file_data, filename, file_size, card_id, user_id, subdomain):
    headers = {"X-Account": subdomain, "X-Auth-Token": TOKEN}
    content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    upload_details = get_s3_upload_details(filename, headers)
    print(upload_details)
    file_url = upload_file_to_s3(
        filename, file_data, content_type, upload_details, headers
    )
    return update_card_with_file(
        card_id, user_id, filename, file_url, file_size, content_type, headers
    )


def get_s3_upload_details(filename, headers):
    print(f"Getting S3 upload details for {filename}")
    response = requests.get(
        f"https://api.codecks.io/s3/sign?objectName={filename}", headers=headers
    )
    response.raise_for_status()
    return response.json()


def upload_file_to_s3(filename, file_data, content_type, upload_details, headers):
    print(f"Uploading {filename} to S3 at {upload_details['signedUrl']}")
    files = {"file": (filename, file_data, content_type)}
    payload = upload_details["fields"]
    payload["Content-Type"] = content_type
    response = requests.post(
        upload_details["signedUrl"], headers=headers, data=payload, files=files
    )
    response.raise_for_status()
    return upload_details["publicUrl"]


def update_card_with_file(
    card_id, user_id, filename, file_url, file_size, content_type, headers
):
    print(f"Updating card {card_id} with file {filename}")
    file_data = {
        "cardId": card_id,
        "userId": user_id,
        "fileData": {
            "fileName": filename,
            "url": file_url,
            "size": file_size,
            "type": content_type,
        },
    }
    response = requests.post(
        "https://api.codecks.io/dispatch/cards/addFile", headers=headers, json=file_data
    )
    response.raise_for_status()
    print("Done!")
    return response


def generate_url(
    subdomain: str, card_title: str, account_seq: Union[Sequence, str, int]
) -> str:
    if isinstance(account_seq, (str, int)):
        account_seq = Sequence(account_seq)
    return f"https://{subdomain}.codecks.io/card/{account_seq}-{card_title.replace(' ', '-')}"


def pascalize(string: str) -> str:
    string = string.replace("_", "")
    return string[0].upper() + string[1:]


def unpascalize(string: str) -> str:
    return "_root" if string.lower() == "root" else string[0].lower() + string[1:]


def is_valid_uuid(s: str) -> bool:
    try:
        uuid.UUID(s)
    except ValueError:
        return False
    return True
