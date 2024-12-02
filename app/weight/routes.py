from flask import render_template
from app.weight import bp
from flask_login import current_user


@bp.route("/weight_view")
def all_records():
    return render_template("weight/weight_view.html")
