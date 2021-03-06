
from argparse import Action
from ast import Lambda, Set, Tuple
from dataclasses import Field
import inspect
from pyclbr import Function
import sys
from typing import Callable, List, TypeVar, Generic
from matplotlib import docstring
import numpy, matplotlib, math
from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty

V = TypeVar("V")

class Identity(Generic[V]):
    """
    Identity is a true universally quantified formula.
    """
    def __init__(self, domain: set[V], formula: Callable, vars: int) -> None:
        """
        :param domain: A set of elements to be quantified
        :param formula: A lambda expression
        :param vars: The number of arguments in the formula
        """
        self.domain = domain
        self.formula = formula
        self.vars = vars

    def __init__(self, domain: set[V], formula: Callable) -> None:
        """
        :param domain: A set of elements to be quantified
        :param formula: A lambda expression
        """
        self.domain = domain
        self.formula = formula
        self.vars = len(inspect.signature(formula).parameters)

    def __call__(self, *args):
        exprs = self.formula(*args)
        for i in range(len(args) - 2):
            if exprs[i] is not exprs[i + 1]:
                return False
        return True

    def __or__(self, other: "Identity") -> "Identity":
        return Identity(self.domain | other.domain, lambda x: self.formula(x) or other.formula(x))

    def is_true(self) -> bool:
        for var in self.domain:
            self.formula(var)

    def __str__(self) -> str:
        var_format = ["x", "y", "z", "w", "t", "u", "v"]
        if self.vars > 6:
            var_format = list(map(lambda i: "x_" + str(i), range(self.vars)))
        print(var_format)
        return "for all {} ∈ {} : {}".format(", ".join([val for val in var_format]), self.domain, self.formula)

    def __repr__(self) -> str:
        return "Identity({}, {})".format(self.domain, self.formula)
