from calculators.app.calculator3 import Calculator3
from calculators.drivers.numpy_handler import NumpyHandler

def calculator3_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator3(numpy_handler)
    return calc
