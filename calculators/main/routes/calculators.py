from flask import Blueprint, jsonify, request
from calculators.app.calculator1 import Calculator1
from calculators.app.calculator1 import Calculator2
from calculators.drivers.numpy_handler import NumpyHandler

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    calc = Calculator1()
    response = calc.calculate(request)
    return jsonify(response), 200

@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
    numpy_handler = NumpyHandler()
    calc = Calculator2(numpy_handler)
    response = calc.calculate(request)
    return jsonify(response), 200