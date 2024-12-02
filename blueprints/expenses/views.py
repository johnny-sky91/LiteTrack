from flask import Blueprint, render_template

expenses_bp = Blueprint("expenses", __name__, template_folder="../../templates")


@expenses_bp.route("/")
def view_expenses():
    return render_template("expenses.html")
