from .custom_nodes.boolean_nodes import FalseNode
from .custom_nodes.boolean_nodes import TrueNode
from .custom_nodes.boolean_nodes import Not
from .custom_nodes.boolean_nodes import And
from .custom_nodes.boolean_nodes import Or
from .custom_nodes.boolean_nodes import Xor
from .custom_nodes.boolean_nodes import Nand
from .custom_nodes.boolean_nodes import Nor
from .custom_nodes.boolean_nodes import BinaryExpression
from .custom_nodes.boolean_nodes import ConditionalBranch

from .custom_nodes.arithmetic_comparison_nodes import LessThan
from .custom_nodes.arithmetic_comparison_nodes import LessThanOrEqualTo
from .custom_nodes.arithmetic_comparison_nodes import EqualTo
from .custom_nodes.arithmetic_comparison_nodes import NotEqualTo
from .custom_nodes.arithmetic_comparison_nodes import GreaterThanOrEqualTo
from .custom_nodes.arithmetic_comparison_nodes import GreaterThan
from .custom_nodes.arithmetic_comparison_nodes import BinaryComparison

from .custom_nodes.string_comparison_nodes import AlphabeticalLessThan
from .custom_nodes.string_comparison_nodes import AlphabeticalLessThanOrEqualTo
from .custom_nodes.string_comparison_nodes import AlphabeticalEqualTo
from .custom_nodes.string_comparison_nodes import AlphabeticalNotEqualTo
from .custom_nodes.string_comparison_nodes import AlphabeticalGreaterThanOrEqualTo
from .custom_nodes.string_comparison_nodes import AlphabeticalGreaterThan
from .custom_nodes.string_comparison_nodes import Contains
from .custom_nodes.string_comparison_nodes import NotContains
from .custom_nodes.string_comparison_nodes import StartsWith
from .custom_nodes.string_comparison_nodes import NotStartsWith
from .custom_nodes.string_comparison_nodes import EndsWith
from .custom_nodes.string_comparison_nodes import NotEndsWith
from .custom_nodes.string_comparison_nodes import StringComparison

NODE_CLASS_MAPPINGS = {
    "BooleanExpression.False": FalseNode,
    "BooleanExpression.True": TrueNode,
    "BooleanExpression.Not": Not,
    "BooleanExpression.And": And,
    "BooleanExpression.Or": Or,
    "BooleanExpression.Xor": Xor,
    "BooleanExpression.Nand": Nand,
    "BooleanExpression.Nor": Nor,
    "BooleanExpression.BinaryExpression": BinaryExpression,
    "BooleanExpression.ConditionalBranch": ConditionalBranch,
    "BooleanExpression.ArithmenticComparison.LessThan": LessThan,
    "BooleanExpression.ArithmenticComparison.LessThanOrEqualTo": LessThanOrEqualTo,
    "BooleanExpression.ArithmenticComparison.EqualTo": EqualTo,
    "BooleanExpression.ArithmenticComparison.NotEqualTo": NotEqualTo,
    "BooleanExpression.ArithmenticComparison.GreaterThanOrEqualTo": GreaterThanOrEqualTo,
    "BooleanExpression.ArithmenticComparison.GreaterThan": GreaterThan,
    "BooleanExpression.ArithmenticComparison.BinaryComparison": BinaryComparison,
    "BooleanExpression.StringComparison.AlphabeticalLessThan": AlphabeticalLessThan,
    "BooleanExpression.StringComparison.AlphabeticalLessThanOrEqualTo": AlphabeticalLessThanOrEqualTo,
    "BooleanExpression.StringComparison.AlphabeticalEqualTo": AlphabeticalEqualTo,
    "BooleanExpression.StringComparison.AlphabeticalNotEqualTo": AlphabeticalNotEqualTo,
    "BooleanExpression.StringComparison.AlphabeticalGreaterThanOrEqualTo": AlphabeticalGreaterThanOrEqualTo,
    "BooleanExpression.StringComparison.AlphabeticalGreaterThan": AlphabeticalGreaterThan,
    "BooleanExpression.StringComparison.Contains": Contains,
    "BooleanExpression.StringComparison.NotContains": NotContains,
    "BooleanExpression.StringComparison.StartsWith": StartsWith,
    "BooleanExpression.StringComparison.NotStartsWith": NotStartsWith,
    "BooleanExpression.StringComparison.EndsWith": EndsWith,
    "BooleanExpression.StringComparison.NotEndsWith": NotEndsWith,
    "BooleanExpression.StringComparison.StringComparison": StringComparison,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BooleanExpression.False": "False",
    "BooleanExpression.True": "True",
    "BooleanExpression.Not": "Not",
    "BooleanExpression.And": "And",
    "BooleanExpression.Or": "Or",
    "BooleanExpression.Xor": "Xor",
    "BooleanExpression.Nand": "Nand",
    "BooleanExpression.Nor": "Nor",
    "BooleanExpression.BinaryExpression": "Binary Expression",
    "BooleanExpression.ConditionalBranch": "Conditional Branch",
    "BooleanExpression.ArithmenticComparison.LessThan": "Less than",
    "BooleanExpression.ArithmenticComparison.LessThanOrEqualTo": " Less than or equal to",
    "BooleanExpression.ArithmenticComparison.EqualTo": "Equal to",
    "BooleanExpression.ArithmenticComparison.NotEqualTo": "Not equal to",
    "BooleanExpression.ArithmenticComparison.GreaterThanOrEqualTo": "Greater than or equal to",
    "BooleanExpression.ArithmenticComparison.GreaterThan": "Greater than",
    "BooleanExpression.ArithmenticComparison.BinaryComparison": "Binary Comparison",
    "BooleanExpression.StringComparison.AlphabeticalLessThan": "Comes before",
    "BooleanExpression.StringComparison.AlphabeticalLessThanOrEqualTo": "Comes before or equal to",
    "BooleanExpression.StringComparison.AlphabeticalEqualTo": "Equal to",
    "BooleanExpression.StringComparison.AlphabeticalNotEqualTo": "Not equal to",
    "BooleanExpression.StringComparison.AlphabeticalGreaterThanOrEqualTo": "Comes after or equal to",
    "BooleanExpression.StringComparison.AlphabeticalGreaterThan": "Comes after",
    "BooleanExpression.StringComparison.Contains": "Contains",
    "BooleanExpression.StringComparison.NotContains": "Does not contain",
    "BooleanExpression.StringComparison.StartsWith": "Starts with",
    "BooleanExpression.StringComparison.NotStartsWith": "Does not Start with",
    "BooleanExpression.StringComparison.EndsWith": "Ends with",
    "BooleanExpression.StringComparison.NotEndsWith": "Does not end with",
    "BooleanExpression.StringComparison.StringComparison": "String Comparison",
}

__all__ = ["NODE_CLASS_MAPPINGS"]
