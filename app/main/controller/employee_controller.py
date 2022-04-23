from flask_restx import Resource

from app.main.service.employee_service import get_all_employees, \
    get_a_employee
from app.main.util.dto import EmployeeDto

api = EmployeeDto.api
_employee = EmployeeDto.employee_with_relationship


@api.route('/')
class EmployeeList(Resource):

    @api.doc('list of registered employees')
    @api.marshal_list_with(_employee)
    def get(self):
        return get_all_employees()


@api.route('/<id>')
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
