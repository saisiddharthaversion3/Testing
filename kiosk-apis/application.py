#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful.utils.cors import crossdomain

import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.decorators = [crossdomain(origin='*')]

from db import database_connection

# Calls database connection
mongo = database_connection()

from apps.facerecognition.views import face_auth
from apps.school.views import version3_school

app.register_blueprint(
    face_auth,
    url_prefix='{prefix}'.format(prefix=config.URL_PREFIX))
app.register_blueprint(
    version3_school,
    url_prefix='{prefix}'.format(prefix=config.URL_PREFIX))

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'])
