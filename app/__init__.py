from flask import Flask, render_template
from flask_login import login_required

from config import Config
from .extensions import db, migrate, login_manager


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Register blueprints here
    from app.auth import bp as auth_bp
    from app.expenses import bp as expenses_bp
    from app.weight import bp as weight_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(expenses_bp)
    app.register_blueprint(weight_bp)

    from app.models import auth, expenses, weight

    @app.route("/")
    @login_required
    def main_page():
        return render_template("index.html")

    return app
