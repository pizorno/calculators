from calculators.app.calculator1 import Calculator2
from calculators.drivers.numpy_handler import NumpyHandler

def calculator2_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator2(numpy_handler)
    return calc