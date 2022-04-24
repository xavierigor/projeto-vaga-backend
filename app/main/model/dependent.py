from flask_restx import Namespace, fields
from sqlalchemy.orm import relationship

from app.main import db


class Dependent(db.Model):
    """ Dependent model for storing dependent related details """
    __tablename__ = 'dependents'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(256), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    employee = relationship('Employee', back_populates='dependents')

    def __init__(self, full_name, employee_id):
        self.full_name = full_name
        self.employee_id = employee_id

    def __repr__(self):
        return f'<Dependent \'{self.full_name}\'>'


class DependentDto:
    api = Namespace('dependent', description='dependent related operations')
    dependent = api.model('dependent', {
        'id': fields.Integer(description='dependent Identifier'),
        'full_name': fields.String(
            required=True, description='dependent full name'),
        'employee_id': fields.Integer(description='employee Identifier'),
    })
