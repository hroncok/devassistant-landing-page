import os

from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static', static_url_path='/landing_page')
app.config['DEBUG'] = True # TODO: disable before deploying on production server
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}'.format(os.path.join('..', 'test.db'))
db = SQLAlchemy(app)

import views
import views_admin

if __name__ == "__main__":
    app.run()
