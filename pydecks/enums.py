from enum import Enum


class _PrintableEnum(Enum):
    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class Operator(_PrintableEnum):
    class EQ:
        """
        value | null
        """

        value = "eq"

    class NEQ:
        """
        value | null
        """

        value = "neq"

    class IN:
        """
        array
        """

        value = "in"

    class NOT_IN:
        """
        array
        """

        value = "notIn"

    class GT:
        """
        ordinal value
        """

        value = "gt"

    class GTE:
        """
        ordinal value
        """

        value = "gte"

    class LT:
        """
        ordinal value
        """

        value = "lt"

    class LTE:
        """
        ordinal value
        """

        value = "lte"

    class IN_OR_NULL:
        """
        array
        """

        value = "inOrNull"

    class CONTAINS:
        """
        string (if field is of type string)
        """

        value = "contains"

    class HAS:
        """
        value (if field is of type array)
        """

        value = "has"

    class OVERLAPS:
        """
        array (if field is of type array)
        """

        value = "overlaps"

    class SEARCH:
        """
        string if field is searchable (so far only available for the content field within the card model)
        """

        value = "search"
