# services/users/project/tests/base.py

from project import db
from project import create_app
from flask_testing import TestCase

app = create_app()


# from project import app, db


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object("project.config.TestingConfig")
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
