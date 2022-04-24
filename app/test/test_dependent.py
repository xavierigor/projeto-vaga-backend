import unittest

from app.main.model.department import Department
from app.main.model.dependent import Dependent
from app.main.model.employee import Employee
from app.test.base import BaseTestCase
from app.test.util import create_instance


def create_employees():
    create_instance(Department, name='Sales')
    create_instance(Department, name='Engineering')
    create_instance(Employee, full_name='John Doe', department_id=1)
    create_instance(Employee, full_name='Marie Curie', department_id=2)


class TestDependent(BaseTestCase):

    def test_model_repr(self):
        create_employees()
        dependent = create_instance(
            Dependent, full_name='Cyrus Wall', employee_id=1)
        self.assertEquals(str(dependent), '<Dependent \'Cyrus Wall\'>')


if __name__ == '__main__':
    unittest.main()
