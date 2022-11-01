from crypt import methods
from flask import Blueprint, render_template, redirect, url_for
import os
import sqlite3
from .helpers import *
from .forms import AppointmentForm


bp = Blueprint("main", __name__, '/')
DB_FILE = os.environ.get("DB_FILE")


@bp.route('/')
def main():

    now = datetime.now()
    return redirect(url_for(".daily", year=now.year, month=now.month, day=now.day))


@bp.route('/<year>/<month>/<day>', methods=["POST", "GET"])
def daily(year, month, day):
    form = AppointmentForm()

    if form.validate_on_submit():
        print("Handling submit")
        handle_submit(form, DB_FILE)

    appointments = load_data(DB_FILE, year, month, day)
    appt_list = format_appointments(appointments)
    return render_template('main.html', rows=appt_list, form=form)
