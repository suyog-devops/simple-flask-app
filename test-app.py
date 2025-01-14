import unittest
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b'Hello, World!')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
