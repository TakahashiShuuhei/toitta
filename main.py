# coding: utf-8

import json

from flask import Flask, make_response


app = Flask(__name__)


@app.route('/api/v1/dummy', methods=['GET'])
def dummy():
    response = make_response()
    response.data = json.dumps({'items': [
        {'name': 'dummy1', 'value': 123},
        {'name': 'dummy2', 'value': 222}
    ]})
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

