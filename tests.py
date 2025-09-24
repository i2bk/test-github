# tests.py
import unittest
from app import app

class TestCalculatorAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Calculator API')
    
    def test_add(self):
        response = self.app.get('/add?a=5&b=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 8)

if __name__ == '__main__':
    unittest.main()