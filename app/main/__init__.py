from flask import Blueprint

bp = Blueprint('main', __name__, template_folder="templates")

from app.main import forms, routes
from app import models