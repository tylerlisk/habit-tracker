from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt

bp = Blueprint('auth', __name__)