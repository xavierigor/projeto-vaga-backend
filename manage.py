import unittest

from flask.cli import FlaskGroup

from app.main import app

app.app_context().push()

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
