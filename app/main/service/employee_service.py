from app.main import db
from app.main.model.employee import Employee


def get_all_employees():
    return Employee.query.all()


def get_a_employee(id):
    return Employee.query.filter_by(id=id).first()


def create_employee(data):
    department = Employee(**data)
    db.session.add(department)
    db.session.commit()
    return department, 201
