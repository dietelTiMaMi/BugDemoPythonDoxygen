from overrides import override
from interfaces import MathOperation
from structures import ComplexNumber


class AddComplex(MathOperation):
    @override
    def execute(self, input_a: ComplexNumber, input_b: ComplexNumber) -> ComplexNumber:
        real = input_a.real + input_b.real
        imaginary = input_a.imaginary + input_b.imaginary
        return ComplexNumber(real, imaginary)
