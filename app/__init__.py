from flask import Flask, render_template

from config import Config
from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    # from app.auth import bp as auth_bp
    from app.expenses import bp as expenses_bp
    from app.weight import bp as weight_bp

    # app.register_blueprint(auth_bp)
    app.register_blueprint(expenses_bp)
    app.register_blueprint(weight_bp)

    @app.route("/")
    def main_page():
        return render_template("index.html")

    return app
