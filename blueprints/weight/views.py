from flask import Blueprint, render_template

weight_bp = Blueprint("weight", __name__, template_folder="../../templates")


@weight_bp.route("/")
def view_weight():
    return render_template("weight.html")
