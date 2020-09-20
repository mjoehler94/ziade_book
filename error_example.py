from flask import Flask, jsonify, request 

# this import was added later as part of the blueprint example
from blueprint_example import *

app = Flask(__name__) 
app.register_blueprint(teams)

# make a custom output for 500 error (invalid params in url)
@app.errorhandler(500)
def error_handling(error):
    print("You done screwed this up!")
    return jsonify({'Error':str(error)})

@app.route('/api') 
def my_microservice(): 
    print(request)
    print(request.environ)
    response = jsonify({'Hello':'Chewbacca'})
    print(response)
    print(response.data)
    return response
 
if __name__ == '__main__': 
    print(app.url_map)
    app.run() 
