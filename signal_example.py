
from flask import Flask, jsonify, g, request_finished
from flask.signals import signals_available

if not signals_available:
    raise RuntimeError("pip install blinker")


app = Flask(__name__)

def finished(sender, response, **extra):
    print('About to send a Response')
    print(response)
    print(response.status)
    return

request_finished.connect(finished)


@app.route('/api')
def my_service():
    return jsonify({'This is': 'my generic service output'})

if __name__ == "__main__":
    app.run()

