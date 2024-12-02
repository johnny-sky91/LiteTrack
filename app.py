from flask import Flask, render_template
from blueprints.expenses.views import expenses_bp
from blueprints.weight.views import weight_bp

app = Flask(__name__)

app.register_blueprint(expenses_bp, url_prefix="/expenses")
app.register_blueprint(weight_bp, url_prefix="/weight")


@app.route("/")
def index():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
