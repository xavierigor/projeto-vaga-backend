from app.main.model.dependent import Dependent


def get_all_dependents():
    return Dependent.query.all()


def get_a_dependent(id):
    return Dependent.query.filter_by(id=id).first()


def get_dependents_by_employee(employee_id):
    result = Dependent.query.filter_by(employee_id=employee_id).all()
    return result
