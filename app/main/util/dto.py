from flask_restx import Namespace, fields


class DependentDto:
    api = Namespace('dependent', description='dependent related operations')
    dependent = api.model('dependent', {
        'id': fields.Integer(description='dependent Identifier'),
        'full_name': fields.String(
            required=True, description='dependent full name'),
        'employee_id': fields.Integer(description='employee Identifier'),
    })


class EmployeeDto:
    api = Namespace('employee', description='employee related operations')
    employee = api.model('employee', {
        'id': fields.Integer(description='employee Identifier'),
        'full_name': fields.String(
            required=True, description='employee full name'),
    })
    employee_with_relationship = api.clone('employee', employee, {
        'department_id': fields.Integer(description='department Identifier'),
    })


class DepartmentDto:
    api = Namespace('department', description='department related operations')
    department = api.model('department', {
        'id': fields.Integer(description='department Identifier'),
        'name': fields.String(required=True, description='department name'),
    })
    full_department = api.model('department', {
        'id': fields.Integer(description='department Identifier'),
        'name': fields.String(required=True, description='department name'),
        'employees': fields.Nested(EmployeeDto.employee)
    })
