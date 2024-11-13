#! /bin/python

import implementations
from interfaces import MathOperation
from structures import ComplexNumber


def do_operation(operation: MathOperation):
    a = ComplexNumber(14, 3)
    b = ComplexNumber(12, 42)

    result = operation.execute(a, b)

    print("Operation:")
    print(type(operation).__name__)
    print("Input:")
    print(a)
    print(b)
    print("Result:")
    print(result)


if __name__ == "__main__":
    mul = implementations.MultiplyComplex()
    add = implementations.AddComplex()

    do_operation(mul)

    print()
    print()

    do_operation(add)
