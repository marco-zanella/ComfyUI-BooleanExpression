class AlphabeticalLessThan:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "STRING",
                    {"default": "", "tooltip": "The first string."},
                ),
                "second": (
                    "STRING",
                    {"default": "", "tooltip": "The second string."},
                ),
                "case_insensitive": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "Tooltip": "Toggles case-insensitive comparison.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/String Comparisons"

    def apply(self, first, second, case_insensitive):
        if case_insensitive:
            first = first.lower()
            second = second.lower()
        return (first < second,)


class AlphabeticalLessThanOrEqualTo:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "STRING",
                    {"default": "", "tooltip": "The first string."},
                ),
                "second": (
                    "STRING",
                    {"default": "", "tooltip": "The second string."},
                ),
                "case_insensitive": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "Tooltip": "Toggles case-insensitive comparison.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/String Comparisons"

    def apply(self, first, second, case_insensitive):
        if case_insensitive:
            first = first.lower()
            second = second.lower()
        return (first <= second,)


class AlphabeticalEqualTo:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "STRING",
                    {"default": "", "tooltip": "The first string."},
                ),
                "second": (
                    "STRING",
                    {"default": "", "tooltip": "The second string."},
                ),
                "case_insensitive": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "Tooltip": "Toggles case-insensitive comparison.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/String Comparisons"

    def apply(self, first, second, case_insensitive):
        if case_insensitive:
            first = first.lower()
            second = second.lower()
        return (first == second,)


class AlphabeticalNotEqualTo:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "STRING",
                    {"default": "", "tooltip": "The first string."},
                ),
                "second": (
                    "STRING",
                    {"default": "", "tooltip": "The second string."},
                ),
                "case_insensitive": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "Tooltip": "Toggles case-insensitive comparison.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/String Comparisons"

    def apply(self, first, second, case_insensitive):
        if case_insensitive:
            first = first.lower()
            second = second.lower()
        return (first != second,)


class AlphabeticalGreaterThanOrEqualTo:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "STRING",
                    {"default": "", "tooltip": "The first string."},
                ),
                "second": (
                    "STRING",
                    {"default": "", "tooltip": "The second string."},
                ),
                "case_insensitive": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "Tooltip": "Toggles case-insensitive comparison.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/String Comparisons"

    def apply(self, first, second, case_insensitive):
        if case_insensitive:
            first = first.lower()
            second = second.lower()
        return (first >= second,)


class AlphabeticalGreaterThan:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "STRING",
                    {"default": "", "tooltip": "The first string."},
                ),
                "second": (
                    "STRING",
                    {"default": "", "tooltip": "The second string."},
                ),
                "case_insensitive": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "Tooltip": "Toggles case-insensitive comparison.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/String Comparisons"

    def apply(self, first, second, case_insensitive):
        if case_insensitive:
            first = first.lower()
            second = second.lower()
        return (first > second,)


class Contains:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "haystack": (
                    "STRING",
                    {"default": "", "tooltip": "The string."},
                ),
                "needle": (
                    "STRING",
                    {"default": "", "tooltip": "The string to search."},
                ),
                "case_insensitive": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "Tooltip": "Toggles case-insensitive comparison.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/String Comparisons"

    def apply(self, haystack, needle, case_insensitive):
        if case_insensitive:
            haystack = haystack.lower()
            needle = needle.lower()
        return (needle in haystack,)


class NotContains:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "haystack": (
                    "STRING",
                    {"default": "", "tooltip": "The string."},
                ),
                "needle": (
                    "STRING",
                    {"default": "", "tooltip": "The string to search."},
                ),
                "case_insensitive": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "Tooltip": "Toggles case-insensitive comparison.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/String Comparisons"

    def apply(self, haystack, needle, case_insensitive):
        if case_insensitive:
            haystack = haystack.lower()
            needle = needle.lower()
        return (needle not in haystack,)


class StartsWith:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "haystack": (
                    "STRING",
                    {"default": "", "tooltip": "The string."},
                ),
                "needle": (
                    "STRING",
                    {"default": "", "tooltip": "The string to search."},
                ),
                "case_insensitive": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "Tooltip": "Toggles case-insensitive comparison.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/String Comparisons"

    def apply(self, haystack, needle, case_insensitive):
        if case_insensitive:
            haystack = haystack.lower()
            needle = needle.lower()
        return (haystack.startswith(needle),)


class NotStartsWith:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "haystack": (
                    "STRING",
                    {"default": "", "tooltip": "The string."},
                ),
                "needle": (
                    "STRING",
                    {"default": "", "tooltip": "The string to search."},
                ),
                "case_insensitive": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "Tooltip": "Toggles case-insensitive comparison.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/String Comparisons"

    def apply(self, haystack, needle, case_insensitive):
        if case_insensitive:
            haystack = haystack.lower()
            needle = needle.lower()
        return (not haystack.startswith(needle),)


class EndsWith:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "haystack": (
                    "STRING",
                    {"default": "", "tooltip": "The string."},
                ),
                "needle": (
                    "STRING",
                    {"default": "", "tooltip": "The string to search."},
                ),
                "case_insensitive": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "Tooltip": "Toggles case-insensitive comparison.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/String Comparisons"

    def apply(self, haystack, needle, case_insensitive):
        if case_insensitive:
            haystack = haystack.lower()
            needle = needle.lower()
        return (haystack.endswith(needle),)


class NotEndsWith:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "haystack": (
                    "STRING",
                    {"default": "", "tooltip": "The string."},
                ),
                "needle": (
                    "STRING",
                    {"default": "", "tooltip": "The string to search."},
                ),
                "case_insensitive": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "Tooltip": "Toggles case-insensitive comparison.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/String Comparisons"

    def apply(self, haystack, needle, case_insensitive):
        if case_insensitive:
            haystack = haystack.lower()
            needle = needle.lower()
        return (not haystack.endswith(needle),)


class StringComparison:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first": (
                    "STRING",
                    {"default": "", "tooltip": "The first string."},
                ),
                "second": (
                    "STRING",
                    {"default": "", "tooltip": "The second string."},
                ),
                "operand": (
                    [
                        "<",
                        "≤",
                        "=",
                        "≠",
                        "≥",
                        ">",
                        "contains",
                        "does not contain",
                        "starts with",
                        "does not start with",
                        "ends with",
                        "does not end with",
                    ],
                    {"default": "<", "tooltip": "The string comparison."},
                ),
                "case_insensitive": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "Tooltip": "Toggles case-insensitive comparison.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply"
    CATEGORY = "Boolean Expressions/String Comparisons"

    def apply(self, first, second, operand, case_insensitive):
        if case_insensitive:
            first = first.lower()
            second = second.lower()
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
            case "contains":
                return (second in first,)
            case "does not contain":
                return (second not in first,)
            case "starts with":
                return (first.startswith(second),)
            case "does not start with":
                return (not first.startswith(second),)
            case "ends with":
                return (first.endswith(second),)
            case "does not end with":
                return (not first.endswith(second),)
            case _:
                return (False,)
