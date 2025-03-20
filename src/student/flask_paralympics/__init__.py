import os

from flask import Flask


def create_app(test_config=None):
    # create the Flask app
    app = Flask(__name__, instance_relative_config=True)
    # configure the Flask app (see later notes on how to generate your own
    # SECRET_KEY)
    app.config.from_mapping(
        SECRET_KEY='J91r0NVa0rzqiErpaEaQQg',
        # Set the location of the database file called paralympics.sqlite
        # which will be in the app's instance folder
        SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(app.instance_path,
                                                            'paralympics.sqlite'),
        # You can change the database location to any other directory by
        # changing the SQLALCHEMY_DATABASE_URI
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
