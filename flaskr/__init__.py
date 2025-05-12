import os

from flask import Flask

def create_app(test_config=None):
    #Crear y configurar la aplicación
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        #Cargar la configuración de la instancia, si existe, cuando no se está probando
        app.config.from_pyfile('config.py', silent=True)
    else:
        #Cargar la configuración de prueba si se pasa en
        app.config.from_mapping(test_config)

    #Asegúrese de que la carpeta de la instancia exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Una página simple que dice hola
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)


    return app
