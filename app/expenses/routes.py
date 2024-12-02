from flask import render_template
from app.expenses import bp
from flask_login import current_user


@bp.route("/expenses_view")
def all_expenses():
    return render_template("expenses/expenses_view.html")
