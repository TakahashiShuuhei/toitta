# coding: utf-8

import json
import os

from flask import Flask, make_response

from toitta.flask_settings import DevConfig, ProdConfig
from toitta.rest import tweet


app = Flask(__name__)
env_flag = os.environ.get('TOITTA_ENV', 'development')
conf = {'development': DevConfig,
        'prodction': ProdConfig}.get(env_flag, DevConfig)
app.config.from_object(conf)
app.register_blueprint(tweet.blueprint)


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

