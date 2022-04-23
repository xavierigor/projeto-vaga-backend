from app.main.model.department import Department


def get_all_departments():
    return Department.query.all()


def get_a_department(id):
    return Department.query.filter_by(id=id).first()
