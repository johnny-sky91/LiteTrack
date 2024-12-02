from flask import render_template
from app.expenses import bp


@bp.route("/expenses_view")
def index():
    return render_template("expenses/expenses_view.html")
