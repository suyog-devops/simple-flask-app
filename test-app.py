import unittest
from app import app  # Assuming your app is in a file named app.py

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        """Set up the Flask test client."""
        self.app = app.test_client()  # Creates a test client
        self.app.testing = True  # Enable testing mode

    def test_hello(self):
        """Test the / route."""
        response = self.app.get('/')  # Send GET request to the root route
        self.assertEqual(response.data, b'Hello, World!')  # Check if the response data is 'Hello, World!'
        self.assertEqual(response.status_code, 200)  # Check if the status code is 200 OK

if __name__ == '__main__':
    unittest.main()
