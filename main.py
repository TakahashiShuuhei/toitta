# coding: utf-8

import os

from flask import Flask

from toitta.flask_settings import DevConfig, ProdConfig
from toitta.rest import tweet, user


app = Flask(__name__)
env_flag = os.environ.get('TOITTA_ENV', 'development')
conf = {'development': DevConfig,
        'production': ProdConfig}.get(env_flag, DevConfig)
app.config.from_object(conf)
app.register_blueprint(tweet.blueprint)
app.register_blueprint(user.blueprint)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

