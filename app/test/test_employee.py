import unittest

from app.main.model.department import Department
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
        with self.client:
            response = self.client.get('/employees/')
            data = response.json
            self.assertEquals(len(data), 2)
            self.assertEquals(response.status_code, 200)
            emp1 = data[0]
            self.assertEquals(emp1['full_name'], 'John Doe')
            self.assertEquals(emp1['department_id'], 1)
            emp2 = data[1]
            self.assertEquals(emp2['full_name'], 'Marie Curie')
            self.assertEquals(emp2['department_id'], 2)

    def test_get_a_employee(self):
        with self.client:
            response = self.client.get('/employees/1')
            data = response.json
            self.assertEquals(data['full_name'], 'John Doe')
            self.assertEquals(data['department_id'], 1)
            self.assertEquals(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
