import unittest

from app.main.model.department import Department
from app.main.model.dependent import Dependent
from app.main.model.employee import Employee
from app.test.base import BaseTestCase
from app.test.util import create_instance


def populate():
    create_instance(Department, name='Sales')
    create_instance(Department, name='Engineering')
    create_instance(Employee, full_name='John Doe', department_id=1)
    create_instance(Employee, full_name='Marie Curie', department_id=2)
    create_instance(Dependent, full_name='Cyrus Wall', employee_id=1)


class TestDependent(BaseTestCase):

    def setUp(self):
        super().setUp()
        populate()

    def test_model_repr(self):
        dependent = Dependent.query.get({'id': 1})
        self.assertEquals(str(dependent), '<Dependent \'Cyrus Wall\'>')


if __name__ == '__main__':
    unittest.main()
