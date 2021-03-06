import unittest 
from basic_flask import app as tested_app 
from functional_test_example import TestApp 

class TestMyApp(unittest.TestCase): 
    def test_help(self): 
        # creating a client to interact with the app 
        app = TestApp(tested_app) 

        # calling /api/ endpoint 
        hello = app.get('/api') 

        # asserting the body 
        self.assertEqual(hello.json['Hello'], 'World!') 

if __name__ == '__main__': 
    unittest.main() 
