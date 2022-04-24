from flask import Blueprint
from flask_restx import Api

from app.main.controller.department_controller import api as department_ns
from app.main.controller.employee_controller import api as employee_ns
from app.main.controller.dependent_controller import api as dependent_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='ACMEVita Departments',
    version='1.0',
    description='A department management API',
    license='MIT',
)

api.add_namespace(department_ns, path='/departments')
api.add_namespace(employee_ns, path='/employees')
api.add_namespace(dependent_ns, path='/dependents')
