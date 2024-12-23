from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # Registrar los blueprints
    from app.controllers.expense_controller import expense_bp
    app.register_blueprint(expense_bp)
    
    with app.app_context():
        db.create_all()
    
    return app