import unittest

from flask import url_for

from app.main.model.department import Department
from app.main.model.employee import Employee
from app.test.base import BaseTestCase
from app.test.util import create_instance


def populate():
    create_instance(Department, name='Human Resources')
    create_instance(Department, name='Sales')


class TestDepartment(BaseTestCase):

    def setUp(self):
        super().setUp()
        populate()

    def test_model_repr(self):
        department = Department.query.get({'id': 1})
        self.assertEquals(str(department), '<Department \'Human Resources\'>')

    def test_list_all_departments(self):
        with self.client:
            path = url_for('api.department_list')
            response = self.client.get(path)
            data = response.json
            self.assertEquals(len(data), 2)
            self.assertEquals(response.status_code, 200)
            self.assertEquals(data[0]['name'], 'Human Resources')
            self.assertEquals(data[1]['name'], 'Sales')

    def test_list_all_departments_full(self):
        create_instance(Employee, full_name='Marie Curie', department_id=1)
        with self.client:
            path = url_for('api.department_list')
            response = self.client.get(path + '?full=true')
            data = response.json
            self.assertEquals(response.status_code, 200)
            self.assertTrue('employees' in data[0])
            employees_eng = data[0]['employees']
            self.assertIsInstance(employees_eng, list)
            self.assertEquals(len(employees_eng), 1)
            self.assertEquals(employees_eng[0]['full_name'], 'Marie Curie')
            employees_sales = data[1]['employees']
            self.assertIsInstance(employees_sales, list)
            self.assertEquals(len(employees_sales), 0)

    def test_get_a_department(self):
        with self.client:
            path = url_for('api.department_detail', id=1)
            response = self.client.get(path)
            data = response.json
            self.assertEquals(data['name'], 'Human Resources')
            self.assertEquals(response.status_code, 200)

    def test_create_a_department(self):
        with self.client:
            path = url_for('api.department_list')
            payload = {'name': 'Engineering'}
            response = self.client.post(
                path, json=payload, headers=self.headers)
            data = response.json
            self.assertEquals(response.status_code, 201)
            self.assertEquals(data['name'], 'Engineering')

    def test_create_an_already_existing_department(self):
        expected_count = Department.query.count()
        with self.client:
            path = url_for('api.department_list')
            payload = {'name': 'Sales'}
            response = self.client.post(
                path, json=payload, headers=self.headers)
            data = response.json
            self.assertEquals(response.status_code, 400)
            self.assertEquals(data['detail'], 'Department already exists')
            actual_count = Department.query.count()
            self.assertEquals(expected_count, actual_count)

    def test_create_a_department_without_required_fields(self):
        expected_count = Department.query.count()
        with self.client:
            path = url_for('api.department_list')
            payload = {'test': 'Sales'}
            response = self.client.post(
                path, json=payload, headers=self.headers)
            data = response.json
            self.assertEquals(response.status_code, 400)
            self.assertEquals(
                data['errors']['name'], '\'name\' is a required property')
            actual_count = Department.query.count()
            self.assertEquals(expected_count, actual_count)


if __name__ == '__main__':
    unittest.main()
