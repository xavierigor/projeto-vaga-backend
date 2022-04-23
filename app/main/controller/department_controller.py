from flask_restx import Resource

from app.main.service.department_service import get_all_departments, \
    get_a_department
from app.main.util.dto import DepartmentDto

api = DepartmentDto.api
_department = DepartmentDto.department


@api.route('/')
class DepartmentList(Resource):

    @api.doc('list of registered departments')
    @api.marshal_list_with(_department, envelope='data')
    def get(self):
        return get_all_departments()


@api.route('/<id>')
@api.param('id', 'The Department identifier')
@api.response(404, 'Department not found')
class Department(Resource):

    @api.doc('get a department')
    @api.marshal_with(_department)
    def get(self, id):
        department = get_a_department(id)
        if not department:
            api.abort(404, 'Department not found')
        return department
