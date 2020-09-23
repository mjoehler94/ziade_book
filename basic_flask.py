from flask import Flask, jsonify, request 

# this import was added later as part of the blueprint example
#from blueprint_example import *

app = Flask(__name__) 
#app.register_blueprint(teams)

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

    app.run(debug=False) 
