from flask import render_template, Blueprint, send_file
from models.client_errors import ValidationError, AuthError, ResourceNotFoundError
from facades.vacation_facade import VacationFacade
from facades.auth_facade import AuthFacade
from flask import request, redirect, url_for, session
from utils.image_handler import ImageHandler

# Managing the entire view
vacations_blueprint = Blueprint("vacations_view", __name__)

# Create facades:
vacations_facade = VacationFacade()
auth_facade = AuthFacade()

# Get all vacations


@vacations_blueprint.route("/vacations", methods=["GET", "POST"])
def vacations():
    try:
        user = session.get("user")
        auth_facade.block_anonymous()
        vacations = vacations_facade.get_all_vacations()
        likes = vacations_facade.how_many_likes_for_vacation()
        vacation_like_status = vacations_facade.get_vacations_with_like_status(
            user["user_id"])
        if request.method == "GET":
            return render_template("vacations.html", active="vacations", vacations=vacations, likes=likes, vacation_like_status=vacation_like_status)
    except AuthError as err:
        return redirect(url_for("auth_view.login", error=err.message))


# Insert vacation
@vacations_blueprint.route("/insert", methods=["GET", "POST"])
def insert():
    vacation_countries = vacations_facade.get_countries_name()
    try:
        auth_facade.block_non_admin()
        if request.method == "GET":
            return render_template("insert.html", vacation_countries=vacation_countries)
        vacations_facade.add_new_vacation()
        return redirect(url_for("vacations_view.vacations"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error=err.message))
    except ValidationError as err:
        return render_template("insert.html", error=err.message, vacation=err.model, vacation_countries=vacation_countries)

# Update vacation


@vacations_blueprint.route("/vacations/update/<int:vacation_id>", methods=["GET", "POST"])
def update(vacation_id):
    vacation_countries = vacations_facade.get_countries_name()
    try:
        auth_facade.block_non_admin()
        if request.method == "GET":
            vacation = vacations_facade.get_one_vacation(vacation_id)
            return render_template("update.html", vacation=vacation, vacation_countries=vacation_countries)
        vacations_facade.update_vacation()
        return redirect(url_for("vacations_view.vacations"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error=err.message))
    except ResourceNotFoundError as err:
        return render_template("404.html", error=err.message)
    except ValidationError as err:
        vacation = vacations_facade.get_one_vacation(vacation_id)
        return render_template("update.html", error=err.message, vacation=vacation, vacation_countries=vacation_countries)


# Delete vacation
@vacations_blueprint.route("/vacations/delete/<int:vacation_id>")
def delete(vacation_id):
    try:
        auth_facade.block_non_admin()
        vacations_facade.delete_vacation(vacation_id)
        return redirect(url_for("vacations_view.vacations"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error=err.message))


# Add like to vacation
@vacations_blueprint.route("/vacations/like/<int:user_id>/<int:vacation_id>", methods=["POST"])
def add_like(user_id, vacation_id):
    try:
        is_liked = vacations_facade.is_user_already_liked_same_vacation(
            user_id, vacation_id)
        if not is_liked:
            vacations_facade.add_like_for_vacation(user_id, vacation_id)
        else:
            vacations_facade.delete_like_for_vacation(user_id, vacation_id)
        session["is_liked"] = is_liked
        return redirect(url_for("vacations_view.vacations", is_liked=is_liked))
    except ResourceNotFoundError as err:
        return render_template("404.html", error=err.message)

# Return image file:


@vacations_blueprint.route("/images/countries/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    # Returns a complete file (an image file with pixels of the image...)
    return send_file(image_path)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Get special vacations
@vacations_blueprint.route("/special_vacations")
def special_locations():
    try:
        auth_facade.block_anonymous()
        special_vacation = vacations_facade.special_locations()
        return render_template("special_vacations.html",
                        vacations=special_vacation)
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))
    
    
# Get culinary vacations
@vacations_blueprint.route("/culinary_vacations")
def culinary_vacations():
    try:
        auth_facade.block_anonymous()
        special_vacation = vacations_facade.culinary_locations()
        return render_template("culinary_vacations.html",
                        vacations=special_vacation)
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))
    
    
# Get winter vacations
@vacations_blueprint.route("/winter_vacations")
def winter_vacations():
    try:
        auth_facade.block_anonymous()
        special_vacation = vacations_facade.winter_vacations()
        return render_template("winter_vacations.html",
                        vacations=special_vacation)
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))
    
    
# Get summer vacations
@vacations_blueprint.route("/summer_vacations")
def summer_vacations():
    try:
        auth_facade.block_anonymous()
        special_vacation = vacations_facade.summer_vacations()
        return render_template("summer_vacations.html",
                        vacations=special_vacation)
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))
    
    
