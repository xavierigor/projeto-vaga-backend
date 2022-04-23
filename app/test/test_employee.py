import unittest

from app.main.model.department import Department
from app.main.model.employee import Employee
from app.test.base import BaseTestCase
from app.test.util import create_instance


class TestEmployee(BaseTestCase):

    def test_model_repr(self):
        create_instance(Department, name='Engineering')
        employee = create_instance(
            Employee, full_name='John Doe', department_id=1)
        self.assertEquals(str(employee), '<Employee \'John Doe\'>')

    def test_list_all_employees(self):
        create_instance(Department, name='Sales')
        create_instance(Department, name='Engineering')
        create_instance(Employee, full_name='John Doe', department_id=1)
        create_instance(Employee, full_name='Marie Curie', department_id=2)
        with self.client:
            response_data = self.client.get('/employees/')
            self.assertEquals(len(response_data.json), 2)
            self.assertEquals(response_data.status_code, 200)
            emp1 = response_data.json[0]
            self.assertEquals(emp1['full_name'], 'John Doe')
            self.assertEquals(emp1['department_id'], 1)
            emp2 = response_data.json[1]
            self.assertEquals(emp2['full_name'], 'Marie Curie')
            self.assertEquals(emp2['department_id'], 2)

    def test_get_a_employee(self):
        create_instance(Department, name='Sales')
        create_instance(Employee, full_name='John Doe', department_id=1)
        with self.client:
            response_data = self.client.get('/employees/1')
            self.assertEquals(response_data.json['full_name'], 'John Doe')
            self.assertEquals(response_data.json['department_id'], 1)
            self.assertEquals(response_data.status_code, 200)


if __name__ == '__main__':
    unittest.main()
