import os
import yaml
from pathlib import Path
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from api.controller.start_controller import start

def create_app():
    root_path, path = Path(__file__).parents[0], ''
    app = Flask(__name__)
    
    root_path = 'api/config'
    doc_path = str(root_path + '/' + 'swagger.yaml')
    swagger_yml = yaml.safe_load(open(doc_path, 'r'))

    app.register_blueprint(get_swaggerui_blueprint('/docs', doc_path,
                            config={'spec': swagger_yml}),
                            url_prefix='/docs')
                            
    app.register_blueprint(start)

    return app
    
app = create_app()

def start_server():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    start_server()
