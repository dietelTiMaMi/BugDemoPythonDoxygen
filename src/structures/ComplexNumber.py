from dataclasses import dataclass


@dataclass
class ComplexNumber:
    real: float
    """The real part of the complex number.
    """
    imaginary: float
    """The imaginary part of the complex number.
    """
