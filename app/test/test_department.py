import unittest

from app.main import db
from app.main.model.department import Department
from app.test.base import BaseTestCase


def create_department(name):
    department = Department(name=name)
    db.session.add(department)
    db.session.commit()
    return department


class TestDepartment(BaseTestCase):

    def test_model_repr(self):
        department = create_department(name='Human Resources')
        self.assertEquals(str(department), '<Department \'Human Resources\'')

    def test_list_all_departments(self):
        create_department(name='Human Resources')
        create_department(name='Sales')
        with self.client:
            response_data = self.client.get('/departments/')
            data = response_data.json['data']
            self.assertEquals(len(data), 2)
            self.assertEquals(response_data.status_code, 200)

    def test_get_a_department(self):
        create_department(name='Human Resources')
        with self.client:
            response_data = self.client.get('/departments/1')
            self.assertEquals(response_data.json['name'], 'Human Resources')
            self.assertEquals(response_data.status_code, 200)


if __name__ == '__main__':
    unittest.main()
