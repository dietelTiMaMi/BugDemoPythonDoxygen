from overrides import override
from interfaces import MathOperation
from structures import ComplexNumber


class MultiplyComplex(MathOperation):
    @override
    def execute(self, input_a: ComplexNumber, input_b: ComplexNumber) -> ComplexNumber:
        real = (input_a.real * input_b.real) - (input_a.imaginary * input_b.imaginary)
        imaginary = (input_a.real * input_b.imaginary) + (
            input_a.imaginary * input_b.real
        )
        return ComplexNumber(real, imaginary)
