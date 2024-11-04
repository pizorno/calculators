from typing import Dict
from calculators.app.calculator2 import Calculator2
from calculators.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    driver = NumpyHandler()
    calculator2 = Calculator2(driver)
    formated_response = calculator2.calculate(mock_request)
    assert isinstance(formated_response, dict)
    assert formated_response == {"data": {"Calculator": 2, "result": 0.08}}