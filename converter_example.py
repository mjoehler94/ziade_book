from flask import Flask, jsonify, request 
from werkzeug.routing import BaseConverter, ValidationError 

_USERS = {'1': 'Tarek', '2': 'Freya'} 
_IDS = {val: id for id, val in _USERS.items()} 

class RegisteredUser(BaseConverter): 
    def to_python(self, value): 
        print("to_python")
        if value in _USERS: 
            return _USERS[value] 
        print("raise error")
        raise ValidationError() 

    def to_url(self, value): 
         print("to_url")
         return _IDS[value] 

app = Flask(__name__) 
app.url_map.converters['registered'] = RegisteredUser 

@app.route('/api/person/<registered:name>') 
def person(name): 
    response = jsonify({'Hello hey': name}) 
    return response 

if __name__ == '__main__': 
	app.run() 
