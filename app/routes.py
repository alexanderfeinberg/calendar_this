from flask import Blueprint, render_template, redirect
import os
import sqlite3
from .helpers import *
bp = Blueprint("main", __name__, '/')
DB_FILE = os.environ.get("DB_FILE")


@bp.route('/')
def main():
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            'SELECT id, name, start_datetime, end_datetime FROM appointments ORDER BY start_datetime')
        appointments = curs.fetchall()

    appt_list = format_appointments(appointments)
    print(appt_list)

    return render_template('main.html', rows=appt_list)
