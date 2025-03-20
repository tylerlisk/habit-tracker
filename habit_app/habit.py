from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user


bp = Blueprint('habit', __name__)