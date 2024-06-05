from flask import render_template, Blueprint

# Managing the entire view
about_blueprint = Blueprint("about_view", __name__)

@about_blueprint.route("/about")
def about():
    return render_template("about_us.html", active = "about")