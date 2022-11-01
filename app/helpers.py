from datetime import datetime


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
