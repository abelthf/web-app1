# services/users/project/tests/test_users.py


import json
import unittest

from project.tests.base import BaseTestCase

from project import db
from project.api.models import User
from project.tests.utils import add_user

"""
funcion de ayuda para agaregar usuarios.
"""

"""
def add_user(username, email):  # nuevo
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user
"""


class TestUserService(BaseTestCase):
    """Tests para el servicio Users."""

    def test_users(self):
        """Asegurando que la ruta /ping se comporta correctamente."""
        response = self.client.get("/users/ping")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("pong!", data["message"])
        self.assertIn("success", data["status"])

    def test_add_user(self):
        """
        Asegurando que un nuevo user pueda ser agregado a la base de datos.
        """
        with self.client:
            response = self.client.post(
                "/users",
                data=json.dumps({
                    "username": "abel.huanca",
                    "email": "abel.huanca@upeu.edu.pe"
                }),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn(
                "abel.huanca@upeu.edu.pe was added!", data["message"])
            self.assertIn("success", data["status"])

    def test_add_user_invalid_json(self):
        """Asegurando que se produzca un error si el objeto JSON está vacio."""
        with self.client:
            response = self.client.post(
                "/users",
                data=json.dumps({}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid payload.", data["message"])
            self.assertIn("fail", data["status"])

    def test_add_user_invalid_json_keys(self):
        """
        Asegurando que se produzca un error si el objeto JSON no tiene un key
        de username.
        """
        with self.client:
            response = self.client.post(
                "/users",
                data=json.dumps({"email": "abel.huanca@upeu.edu.pe"}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid payload.", data["message"])
            self.assertIn("fail", data["status"])

    def test_add_user_duplicate_email(self):
        """Asegurando que se produzca un error si el email ya existe."""
        with self.client:
            self.client.post(
                "/users",
                data=json.dumps({
                    "username": "abel.huanca",
                    "email": "abel.huanca@upeu.edu.pe"
                }),
                content_type="application/json",
            )
            response = self.client.post(
                "/users",
                data=json.dumps({
                    "username": "abel.huanca",
                    "email": "abel.huanca@upeu.edu.pe"
                }),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Sorry. That email already exists.", data["message"])
            self.assertIn("fail", data["status"])

    def test_single_user(self):
        """Asegurar obtener un usuario se comporte correctamente."""
        # user = User(username='abel.huanca', email='abel.huanca@upeu.edu.pe')
        user = add_user('abel.huanca', 'abel.huanca@upeu.edu.pe')
        # db.session.add(user)
        # db.session.commit()
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('abel.huanca', data['data']['username'])
            self.assertIn('abel.huanca@upeu.edu.pe', data['data']['email'])
            self.assertIn('success', data['status'])

    """
    GET single user
    """

    def test_single_user_no_id(self):
        """Asegurando el error se produzca si no se proporciona un id."""
        with self.client:
            response = self.client.get('/users/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user_icorrect_id(self):
        """Asegurando que el error se produza si el id no existe."""
        with self.client:
            response = self.client.get('/users/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])
    """
    GET all users
    """

    def test_all_users(self):
        """
        Asegurando que se obtienen todos los usuarios correctamente.
        """
        add_user('abel.huanca', 'abel.huanca@upeu.edu.pe')
        add_user('fredy', 'abelthf@gmail.com')
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('abel.huanca', data['data']['users'][0]['username'])
            self.assertIn(
                'abel.huanca@upeu.edu.pe', data['data']['users'][0]['email'])
            self.assertIn('fredy', data['data']['users'][1]['username'])
            self.assertIn(
                'abelthf@gmail.com', data['data']['users'][1]['email'])
            self.assertIn('success', data['status'])

    def test_main_no_users(self):
        """Asegurando que la ruta principal se comporte correctamente
        cuando no se hayan agregado usuarios a la base de datos."""

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'All Users', response.data)
        self.assertIn(b'<p>No users!</p>', response.data)

    def test_main_with_users(self):
        """Asegurando que la ruta principal se comporte correctamente cuando se
        hayan agregado usuarios a la base de datos."""

        add_user('abel.huanca', 'abel.huanca@upeu.edu.pe')
        add_user('abelthf', 'abelthf@gmail.com')
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All Users', response.data)
            self.assertNotIn(b'<p>No users!</p>', response.data)
            self.assertIn(b'abel.huanca', response.data)
            self.assertIn(b'abelthf', response.data)

    def test_main_add_user(self):
        """
        Asegurando que se pueda agregar un nuevo usuario a la base de datos
        mediante una solicitud POST.
        """
        with self.client:
            response = self.client.post(
                '/',
                data=dict(username='danmichael', email='danmichael@test.com'),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
