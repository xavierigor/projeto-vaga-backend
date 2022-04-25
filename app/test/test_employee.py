import json
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


class TestEmployee(BaseTestCase):

    def setUp(self):
        super().setUp()
        populate()

    def test_model_repr(self):
        employee = Employee.query.get({'id': 1})
        self.assertEquals(str(employee), '<Employee \'John Doe\'>')

    def test_list_all_employees(self):
        create_instance(Dependent, full_name='Cyrus Wall', employee_id=1)
        with self.client:
            path = url_for('api.employee_list')
            response = self.client.get(path)
            data = response.json
            self.assertEquals(len(data), 2)
            self.assertEquals(response.status_code, 200)
            emp1 = data[0]
            self.assertEquals(emp1['full_name'], 'John Doe')
            self.assertEquals(emp1['department_id'], 1)
            self.assertTrue(emp1['have_dependents'])
            emp2 = data[1]
            self.assertEquals(emp2['full_name'], 'Marie Curie')
            self.assertEquals(emp2['department_id'], 2)
            self.assertFalse(emp2['have_dependents'])

    def test_get_a_employee(self):
        with self.client:
            path = url_for('api.employee_detail', id=1)
            response = self.client.get(path)
            data = response.json
            self.assertEquals(data['full_name'], 'John Doe')
            self.assertEquals(data['department_id'], 1)
            self.assertEquals(response.status_code, 200)

    def test_get_employees_dependents(self):
        create_instance(Employee, full_name='Clifford Price', department_id=2)
        create_instance(Dependent, full_name='Cyrus Wall', employee_id=1)
        create_instance(Dependent, full_name='Cassia Callaghan', employee_id=2)
        with self.client:
            path = url_for('api.employee_dependents', id=1)
            response = self.client.get(path)
            data = response.json
            self.assertIsInstance(data, list)
            self.assertEquals(len(data), 1)
            self.assertEquals(response.status_code, 200)
            dependent = data[0]
            self.assertEquals(dependent['full_name'], 'Cyrus Wall')
            self.assertEquals(dependent['employee_id'], 1)
            path = url_for('api.employee_dependents', id=3)
            response = self.client.get(path)
            data = response.json
            self.assertIsInstance(data, list)
            self.assertEquals(len(data), 0)
            self.assertEquals(response.status_code, 200)

    def test_create_a_employee(self):
        with self.client:
            path = url_for('api.employee_list')
            payload = {'full_name': 'Neive Bates', 'department_id': 2}
            response = self.client.post(
                path, json=payload, headers=self.headers)
            data = response.json
            self.assertEquals(response.status_code, 201)
            self.assertEquals(data['full_name'], payload['full_name'])
            self.assertEquals(data['department_id'], payload['department_id'])
            self.assertFalse(data['have_dependents'])

    def test_create_a_employee_without_required_fields(self):
        expected_count = Employee.query.count()
        with self.client:
            path = url_for('api.employee_list')
            payload = {'test': 'Neive Bates', 'department_id': 2}
            response = self.client.post(
                path, json=payload, headers=self.headers)
            data = response.json
            self.assertEquals(response.status_code, 400)
            self.assertEquals(
                data['errors']['full_name'],
                '\'full_name\' is a required property')

            payload = {'full_name': 'Neive Bates', 'test': 2}
            response = self.client.post(
                path, json=payload, headers=self.headers)
            data = response.json
            self.assertEquals(response.status_code, 400)
            self.assertEquals(
                data['errors']['department_id'],
                '\'department_id\' is a required property')

            payload = {}
            response = self.client.post(
                path, json=payload, headers=self.headers)
            data = response.json
            self.assertEquals(response.status_code, 400)
            self.assertEquals(len(data['errors']), 2)
            self.assertIn('full_name', data['errors'])
            self.assertIn('department_id', data['errors'])

            actual_count = Employee.query.count()
            self.assertEquals(expected_count, actual_count)


if __name__ == '__main__':
    unittest.main()
