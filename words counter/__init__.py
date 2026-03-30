import os
from flask import Flask
from mainCode import words

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    #for_testing_Route
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    db.init_app(app)

    #Blueprint_registration
    app.register_blueprint(words.bp)
    return app