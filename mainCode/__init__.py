import os
from flask import Flask
from . import todoRoutes

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        UPLOAD_FOLDER = os.path.join(app.root_path, 'static'),
        send_file_max_age_default=0
    )


    os.makedirs(app.instance_path, exist_ok=True)

    # ""os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)""
    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    app.register_blueprint(todoRoutes.bp)
    return app
