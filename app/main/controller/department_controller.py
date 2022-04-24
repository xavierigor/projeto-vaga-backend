from flask_restx import Resource, marshal

from app.main.model.department import DepartmentDto
from app.main.service.department_service import get_all_departments, \
    get_a_department

api = DepartmentDto.api
_department = DepartmentDto.department
_full_department = DepartmentDto.full_department

parser = api.parser()
parser.add_argument(
    'full', type=lambda v: v.lower() == 'true', default=False, location='args',
    help="""If true, shows all the department information including
        employee's full names and if they have any dependent""")


@api.route('/')
class DepartmentList(Resource):

    @api.doc('list of registered departments')
    @api.expect(parser, )
    def get(self):
        args = parser.parse_args()
        if args['full'] is True:
            return marshal(get_all_departments(), _full_department)
        return marshal(get_all_departments(), _department)


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
