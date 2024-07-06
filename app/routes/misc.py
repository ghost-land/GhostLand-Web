from flask import Blueprint, redirect
from datetime import datetime
from run import settings

misc_bp = Blueprint('misc', __name__)


@misc_bp.route("/discord")
@misc_bp.route("/discord/")
@misc_bp.route("/dsc")
@misc_bp.route("/dsc/")
def discord():
    return redirect(settings['site']['settings'].get('discord-url', '/'), code=302)