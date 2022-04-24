from flask_restx import Resource

from app.main.model.dependent import DependentDto
from app.main.model.employee import EmployeeDto
from app.main.service.dependent_service import get_dependents_by_employee
from app.main.service.employee_service import get_all_employees, \
    get_a_employee

api = EmployeeDto.api
_employee = EmployeeDto.employee_with_relationship
_dependent = DependentDto.dependent


@api.route('/', endpoint='employee_list')
class EmployeeList(Resource):

    @api.doc('list of registered employees')
    @api.marshal_list_with(_employee)
    def get(self):
        return get_all_employees()


@api.route('/<id>', endpoint='employee_detail')
@api.param('id', 'The Employee identifier')
@api.response(404, 'Employee not found')
class Employee(Resource):

    @api.doc('get a employee')
    @api.marshal_with(_employee)
    def get(self, id):
        employee = get_a_employee(id)
        if not employee:
            api.abort(404, 'Employee not found')
        return employee


@api.route('/<id>/dependents', endpoint='employee_dependents')
@api.param('id', 'The Employee identifier')
class EmployeesDependentList(Resource):

    @api.doc('get employee\'s dependents')
    @api.marshal_with(_dependent)
    def get(self, id):
        dependents = get_dependents_by_employee(id)
        return dependents
