import unittest

from flask.cli import FlaskGroup

from app import app
from app.main.model.department import Department
from app.main.model.employee import Employee

cli = FlaskGroup(app)


@cli.command('test')
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    cli()
