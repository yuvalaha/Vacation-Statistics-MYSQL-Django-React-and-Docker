from flask import render_template, Blueprint

# Managing the entire view
join_us_blueprint = Blueprint("join_us_view", __name__)

@join_us_blueprint.route("/join_us")
def join_us():
    return render_template("join_us.html", active = "join_us")