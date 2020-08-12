import datetime


def format_datetime(date_string):
    new_date = datetime.datetime.strptime(date_string, "%b %d %Y %I:%M%p")
    formated_date = new_date.strftime("%Y-%m-%d %H:%M:%S")
    return formated_date


print(format_datetime("Feb 12 2019 2:41PM"))
