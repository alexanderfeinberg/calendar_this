from crypt import methods
from flask import Blueprint, render_template, redirect
import os
import sqlite3
from .helpers import *
from .forms import AppointmentForm


bp = Blueprint("main", __name__, '/')
DB_FILE = os.environ.get("DB_FILE")


@bp.route('/', methods=["GET", "POST"])
def main():
    form = AppointmentForm()

    if form.validate_on_submit():
        print("Handling submit")
        handle_submit(form, DB_FILE)

    appointments = load_data(DB_FILE)
    appt_list = format_appointments(appointments)
    print(appt_list)

    return render_template('main.html', rows=appt_list, form=form)
