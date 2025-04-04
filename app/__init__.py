from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Importa el módulo

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)  # Habilita CORS para la app
    # Configuración de la base de datos
    CORS(app, resources={
        r"/productos*": {
            "origins": ["http://localhost:5500"],
            "methods": ["GET", "POST", "PATCH", "DELETE"],
            "allow_headers": ["Content-Type"]
        }
    })
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventario.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    # Importar rutas después de crear la app para evitar circular imports
    from .routes import productos_bp
    app.register_blueprint(productos_bp)
    
    return app