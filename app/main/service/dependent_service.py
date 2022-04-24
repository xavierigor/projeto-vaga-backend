from app.main.model.dependent import Dependent


def get_dependents_by_employee(employee_id):
    result = Dependent.query.filter_by(employee_id=employee_id).all()
    return result
