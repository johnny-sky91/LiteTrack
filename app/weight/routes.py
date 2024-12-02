from flask import render_template
from app.weight import bp


@bp.route("/weight_view")
def index():
    return render_template("weight/weight_view.html")
