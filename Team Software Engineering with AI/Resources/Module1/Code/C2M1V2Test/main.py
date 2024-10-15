import unittest
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify(message=f"Hello, {name}!")


class FlaskTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_greet_with_name(self):
        # Caso de prueba: la API debe devolver un saludo adecuado para un nombre dado
        response = self.app.get('/api/greet/John')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, John!"})

    def test_greet_with_empty_name(self):
        # Caso de prueba: la API debe manejar el caso donde el nombre está vacío
        response = self.app.get('/api/greet/')
        self.assertEqual(response.status_code, 404)

    def test_greet_with_special_characters(self):
        # Caso de prueba: la API debe manejar nombres con caracteres especiales
        response = self.app.get('/api/greet/John@Doe')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, John@Doe!"})

    def test_greet_with_long_name(self):
        # Caso de prueba: la API debe manejar nombres largos
        long_name = "A" * 256
        response = self.app.get(f'/api/greet/{long_name}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": f"Hello, {long_name}!"})

    def test_greet_with_numeric_name(self):
        # Caso de prueba: la API debe manejar nombres numéricos
        response = self.app.get('/api/greet/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, 12345!"})

    def test_greet_with_name_with_spaces(self):
        # Caso de prueba: la API debe manejar nombres con espacios correctamente
        response = self.app.get('/api/greet/John%20Doe')  # "%20" es el encoding para espacio en URLs
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, John Doe!"})

    def test_greet_with_non_latin_characters(self):
        # Caso de prueba: la API debe manejar nombres con caracteres no latinos
        response = self.app.get('/api/greet/Иван')  # Nombre en cirílico
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, Иван!"})

        response = self.app.get('/api/greet/张伟')  # Nombre en chino
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, 张伟!"})

        response = self.app.get('/api/greet/山田太郎')  # Nombre en japonés
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, 山田太郎!"})


if __name__ == '__main__':
    unittest.main()
