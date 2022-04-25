from flask import request
from flask_restx import Resource

from app.main.model.dependent import DependentDto
from app.main.service.dependent_service import get_all_dependents, \
    get_a_dependent, create_dependent

api = DependentDto.api
_dependent = DependentDto.dependent


@api.route('/', endpoint='dependent_list')
class DependentList(Resource):

    @api.doc('list of registered dependents')
    @api.marshal_list_with(_dependent)
    def get(self):
        return get_all_dependents()

    @api.response(
        description='Dependent successfully created',
        model=_dependent,
        code=201
    )
    @api.doc('create a new dependent')
    @api.expect(_dependent, validate=True)
    @api.marshal_with(_dependent)
    def post(self):
        return create_dependent(request.json)


@api.route('/<id>', endpoint='dependent_detail')
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
