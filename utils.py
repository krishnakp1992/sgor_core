from fastapi_sqlalchemy import db
from sgor_core.models import User

def check_if_user_exists(email):
    user = db.session.query(User).filter_by(email=email).first()
    return user
