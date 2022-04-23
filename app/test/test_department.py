import unittest

from app.main.model.department import Department
from app.main.model.employee import Employee
from app.test.base import BaseTestCase
from app.test.util import create_instance


class TestDepartment(BaseTestCase):

    def test_model_repr(self):
        department = create_instance(Department, name='Human Resources')
        self.assertEquals(str(department), '<Department \'Human Resources\'>')

    def test_list_all_departments(self):
        create_instance(Department, name='Human Resources')
        create_instance(Department, name='Sales')
        with self.client:
            response_data = self.client.get('/departments/')
            self.assertEquals(len(response_data.json), 2)
            self.assertEquals(response_data.status_code, 200)
            self.assertEquals(response_data.json[0]['name'], 'Human Resources')
            self.assertEquals(response_data.json[1]['name'], 'Sales')

    def test_list_all_departments_full(self):
        create_instance(Department, name='Engineering')
        create_instance(Department, name='Sales')
        create_instance(Employee, full_name='Marie Curie', department_id=1)
        with self.client:
            response_data = self.client.get('/departments/?full=true')
            json_data = response_data.json
            self.assertEquals(response_data.status_code, 200)
            self.assertTrue('employees' in json_data[0])
            employees_eng = json_data[0]['employees']
            self.assertTrue(isinstance(employees_eng, list))
            self.assertEquals(len(employees_eng), 1)
            self.assertEquals(employees_eng[0]['full_name'], 'Marie Curie')
            employees_sales = json_data[1]['employees']
            self.assertTrue(isinstance(employees_sales, list))
            self.assertEquals(len(employees_sales), 0)

    def test_get_a_department(self):
        create_instance(Department, name='Human Resources')
        with self.client:
            response_data = self.client.get('/departments/1')
            self.assertEquals(response_data.json['name'], 'Human Resources')
            self.assertEquals(response_data.status_code, 200)


if __name__ == '__main__':
    unittest.main()
