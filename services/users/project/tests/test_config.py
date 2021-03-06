# services/users/project/tests/test_config.py

from flask_testing import TestCase
from flask import current_app
from project import create_app
import os
import unittest

app = create_app()


# from project import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object("project.config.DevelopmentConfig")
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config["SECRET_KEY"] == "my_key")
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
                "DATABASE_URL")
        )
        self.assertTrue(app.config['DEBUG_TB_ENABLED'])  # nuevo


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object("project.config.TestingConfig")
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config["SECRET_KEY"] == "my_key")
        self.assertTrue(app.config["TESTING"])
        self.assertFalse(app.config["PRESERVE_CONTEXT_ON_EXCEPTION"])
        self.assertTrue(
            app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
                "DATABASE_TEST_URL")
        )
        self.assertFalse(app.config['DEBUG_TB_ENABLED'])  # nuevo


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object("project.config.ProductionConfig")
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config["SECRET_KEY"] == "my_key")
        self.assertFalse(app.config["TESTING"])
        self.assertFalse(app.config['DEBUG_TB_ENABLED'])  # nuevo


if __name__ == "__main__":
    unittest.main()
