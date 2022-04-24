from flask_restx import Namespace, fields
from sqlalchemy.orm import relationship

from app.main import db
from app.main.model.employee import EmployeeDto


class Department(db.Model):
    """ Department model for storing department related details """
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    employees = relationship('Employee', back_populates='department')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Department \'{self.name}\'>'


class DepartmentDto:
    api = Namespace('department', description='department related operations')
    department = api.model('department', {
        'id': fields.Integer(readonly=True, description='department Identifier'),
        'name': fields.String(required=True, description='department name'),
    })
    full_department = api.inherit('Department', department, {
        'employees': fields.Nested(EmployeeDto.employee, readonly=True)
    })
