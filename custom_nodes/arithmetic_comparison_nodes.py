class LessThan:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The first number."},
                ),
                "second": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The second number."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/Arithmetic Comparisons"

    def apply(self, first, second):
        return (first < second,)


class LessThanOrEqualTo:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The first number."},
                ),
                "second": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The second number."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/Arithmetic Comparisons"

    def apply(self, first, second):
        return (first <= second,)


class EqualTo:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The first number."},
                ),
                "second": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The second number."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/Arithmetic Comparisons"

    def apply(self, first, second):
        return (first == second,)


class NotEqualTo:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The first number."},
                ),
                "second": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The second number."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/Arithmetic Comparisons"

    def apply(self, first, second):
        return (first != second,)


class GreaterThanOrEqualTo:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The first number."},
                ),
                "second": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The second number."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/Arithmetic Comparisons"

    def apply(self, first, second):
        return (first >= second,)


class GreaterThan:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The first number."},
                ),
                "second": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The second number."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/Arithmetic Comparisons"

    def apply(self, first, second):
        return (first > second,)


class BinaryComparison:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The first number."},
                ),
                "second": (
                    "INT,FLOAT",
                    {"default": 0.0, "tooltip": "The second number."},
                ),
                "operand": (
                    ["<", "≤", "=", "≠", "≥", ">"],
                    {"default": "<", "tooltip": "The arithmetic comparison."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/Arithmetic Comparisons"

    def apply(self, first, second, operand):
        match operand:
            case "<":
                return (first < second,)
            case "≤":
                return (first <= second,)
            case "=":
                return (first == second,)
            case "≠":
                return (first != second,)
            case "≥":
                return (first >= second,)
            case ">":
                return (first > second,)
            case _:
                return (False,)
