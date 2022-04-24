from sqlalchemy.orm import relationship

from app.main import db


class Employee(db.Model):
    """ Employee model for storing employee related details """
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(256), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    department = relationship('Department', back_populates='employees')
    dependents = relationship('Dependent', back_populates='employee')

    def __init__(self, full_name, department_id):
        self.full_name = full_name
        self.department_id = department_id

    def __repr__(self):
        return f'<Employee \'{self.full_name}\'>'
