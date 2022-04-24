from app.main import db
from app.main.model.department import Department


def get_all_departments():
    return Department.query.all()


def get_a_department(id):
    return Department.query.filter_by(id=id).first()


def create_department(data):
    already_exists = Department.query.filter_by(**data).scalar() is not None
    if already_exists:
        res_data = {'detail': 'Department already exists'}
        return res_data, 400
    department = Department(**data)
    db.session.add(department)
    db.session.commit()
    return department, 201
