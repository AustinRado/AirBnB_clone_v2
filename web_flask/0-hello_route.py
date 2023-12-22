#!/usr/bin/python3
'''
Server
-web application must be listening on 0.0.0.0, port 5000
-routes:
    /: display “Hello HBNB!”
-use the option strict_slashes=False in your route definition
'''

try:
    from flask import Flask
except ImportError as e:
    print(e)

app = Flask(__name__)


@app.route('/')
def hello_HBNB():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
