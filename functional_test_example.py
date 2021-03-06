import unittest 
import json 
from basic_flask import app as tested_app 

class TestApp(unittest.TestCase): 
    def test_help(self): 
        # creating a FlaskClient instance to interact with the app 
        app = tested_app.test_client() 

        # calling /api/ endpoint 
        hello = app.get('/api') 

        # asserting the body 
        body = json.loads(str(hello.data, 'utf8')) 
        self.assertEqual(body['Hello'], 'Chewbacca!') 

if __name__ == '__main__': 
    unittest.main() 
