from flask import render_template, Blueprint

# Managing the entire view
reviews_blueprint = Blueprint("reviews_view", __name__)

@reviews_blueprint.route("/reviews")
def reviews():
    return render_template("reviews.html", active = "reviews")