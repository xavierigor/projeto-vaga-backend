from flask_restx import Namespace, fields


class DepartmentDto:
    api = Namespace('department', description='department related operations')
    department = api.model('department', {
        'id': fields.String(description='department Identifier'),
        'name': fields.String(required=True, description='department name'),
    })
