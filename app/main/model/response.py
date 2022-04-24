from flask_restx import Namespace, fields


ns = Namespace('response', description='response related operations')


class ResponseDto:
    error = ns.model('response', {
        'detail': fields.String(
            readonly=True, description='information about the response'),
    })
