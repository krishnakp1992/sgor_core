import datetime
from fastapi_sqlalchemy import db
from sgor_core.models import User

def check_if_user_exists(email):
    user = db.session.query(User).filter_by(email=email).first()
    return user


def find_days_between_dates(start_time, end_time):
    time_difference = end_time - start_time
    days = time_difference.days
    seconds = time_difference.seconds
    if seconds > 0:
        days += 1
    return days
