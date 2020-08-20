"""
Views and routes for the app.
"""

from flask import Flask, render_template, request, Blueprint, url_for

bp = Blueprint('views', __name__, url_prefix='/')


@bp.route('/')
@bp.route('/index')
def index():
    """index page, 'About' """
    return render_template('index.html')