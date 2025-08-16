class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False


any_type = AnyType("*")


class FalseNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("false",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions"

    def apply(self):
        return (False,)


class TrueNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("true",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions"

    def apply(self):
        return (True,)


class Not:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "Boolean value to negate."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("negation",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions"

    def apply(self, value):
        return (not value,)


class And:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "The first boolean value."},
                ),
                "second": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "The second boolean value."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("and",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions"

    def apply(self, first, second):
        return (first and second,)


class Or:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "The first boolean value."},
                ),
                "second": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "The second boolean value."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("or",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions"

    def apply(self, first, second):
        return (first or second,)


class Xor:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "The first boolean value."},
                ),
                "second": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "The second boolean value."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("xor",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions"

    def apply(self, first, second):
        return (first != second,)


class Nand:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "The first boolean value."},
                ),
                "second": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "The second boolean value."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("nand",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions"

    def apply(self, first, second):
        return (not (first and second),)


class Nor:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "The first boolean value."},
                ),
                "second": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "The second boolean value."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("nor",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions"

    def apply(self, first, second):
        return (not (first or second),)


class BinaryExpression:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "The first boolean value."},
                ),
                "second": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "The second boolean value."},
                ),
                "operand": (
                    ["and", "or", "xor", "nand", "nor"],
                    {"default": "and", "tooltip": "The boolean operation."},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions"

    def apply(self, first, second, operand):
        match operand:
            case "and":
                return (first and second,)
            case "or":
                return (first or second,)
            case "xor":
                return (first != second,)
            case "nand":
                return (not (first and second),)
            case "nor":
                return (not (first or second),)
            case _:
                return (False,)


class ConditionalBranch:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "condition": (
                    "BOOLEAN",
                    {"default": True, "tooltip": "The boolean condition."},
                ),
                "if_true": (
                    any_type,
                    {"tooltip": "Value to return if condition is met."},
                ),
                "if_false": (
                    any_type,
                    {"tooltip": "Value to return if condition is not met."},
                ),
            }
        }

    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ("result",)
    FUNCTION = "branch"
    CATEGORY = "Boolean Expressions"

    def branch(self, condition, if_true, if_false):
        return (if_true if condition else if_false,)

    @classmethod
    def IS_CHANGED(s, condition, if_true, if_false):
        return (if_true if condition else if_false,)
