from datetime import datetime


def format_datetime(date_string):
    return datetime.strptime(date_string, "%b %d %Y %I:%M%p")


print(format_datetime("Feb 12 2019 2:41PM"))
