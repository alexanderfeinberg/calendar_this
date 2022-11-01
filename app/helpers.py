from datetime import datetime, timedelta
import sqlite3


def handle_submit(form, DB_FILE):
    params = {
        'name': form.name.data,
        'start_datetime': datetime.combine(form.start_date.data, form.start_time.data),
        'end_datetime': datetime.combine(form.end_date.data, form.end_time.data),
        'description': form.description.data,
        'private': form.private.data
    }

    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute("""
        INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
        VALUES (:name, :start_datetime, :end_datetime, :description, :private)

        """, {'name': params['name'], 'start_datetime': params['start_datetime'], 'end_datetime': params['end_datetime'], 'description': params['description'], 'private': params['private']})


def convert_to_date(date):
    date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    return date_obj


def format_appointments(appointments):
    appt_list = []
    for appt in appointments:
        start_date = convert_to_date(appt[2])
        end_date = convert_to_date(appt[3])
        appt_list.append(
            {'id': appt[0], 'name': appt[1], 'start_datetime': start_date, 'end_datetime': end_date, 'start_date_abv': start_date.strftime('%H:%M'), 'end_date_abv': end_date.strftime('%H:%M')})
    return appt_list


def load_data(DB_FILE, year, month, day):
    date = datetime(int(year), int(month), int(day))
    delta = timedelta(days=1)
    next_day = date+delta
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            'SELECT id, name, start_datetime, end_datetime FROM appointments WHERE start_datetime BETWEEN :date AND :next_day ORDER BY start_datetime', {'date': date, 'next_day': next_day})
        appointments = curs.fetchall()
    return appointments
