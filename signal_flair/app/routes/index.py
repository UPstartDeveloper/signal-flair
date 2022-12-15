from flask import render_template, session

from ..utils import utils


def home():
    """Controller function for the home page route!"""
    utils.check_session_var("error")

    return render_template("index.html", session=session)
