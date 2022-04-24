import unittest

from flask import url_for

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
    create_instance(Dependent, full_name='Cassia Callaghan', employee_id=2)


class TestDependent(BaseTestCase):

    def setUp(self):
        super().setUp()
        populate()

    def test_model_repr(self):
        dependent = Dependent.query.get({'id': 1})
        self.assertEquals(str(dependent), '<Dependent \'Cyrus Wall\'>')

    def test_list_all_dependents(self):
        with self.client:
            path = url_for('api.dependent_list')
            response = self.client.get(path)
            data = response.json
            self.assertIsInstance(data, list)
            self.assertEquals(len(data), 2)
            self.assertEquals(response.status_code, 200)
            dependent1 = data[0]
            self.assertEquals(dependent1['full_name'], 'Cyrus Wall')
            self.assertEquals(dependent1['employee_id'], 1)
            dependent2 = data[1]
            self.assertEquals(dependent2['full_name'], 'Cassia Callaghan')
            self.assertEquals(dependent2['employee_id'], 2)

    def test_get_a_dependent(self):
        with self.client:
            path = url_for('api.dependent_detail', id=1)
            response = self.client.get(path)
            data = response.json
            self.assertIsInstance(data, dict)
            self.assertEquals(response.status_code, 200)
            self.assertEquals(data['full_name'], 'Cyrus Wall')
            self.assertEquals(data['employee_id'], 1)


if __name__ == '__main__':
    unittest.main()
