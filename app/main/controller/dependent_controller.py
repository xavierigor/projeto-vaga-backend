from flask_restx import Resource

from app.main.model.dependent import DependentDto
from app.main.service.dependent_service import get_all_dependents, \
    get_a_dependent

api = DependentDto.api
_dependent = DependentDto.dependent


@api.route('/')
class DependentList(Resource):

    @api.doc('list of registered dependents')
    @api.marshal_list_with(_dependent)
    def get(self):
        return get_all_dependents()


@api.route('/<id>')
@api.param('id', 'The Dependent identifier')
@api.response(404, 'Dependent not found')
class Dependent(Resource):

    @api.doc('get a dependent')
    @api.marshal_with(_dependent)
    def get(self, id):
        dependent = get_a_dependent(id)
        if not dependent:
            api.abort(404, 'Dependent not found')
        return dependent
