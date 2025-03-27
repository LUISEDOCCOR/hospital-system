from flask import  redirect, url_for, session
from functools import wraps
from models.person_model import PersonModel

def requires_login(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if "user_id" not in session or "name" not in session  or "email" not in session :
            return redirect(url_for("auth.index"))
        else:
            return f(*args, **kwargs)
    return decorator

def only_user_type(type: str):
    user = PersonModel.get_by_id(int(session["user_id"]))
    if user:
        return user.type == type
    else:
        return

def only_admins(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if not only_user_type("admin") :
            return redirect(url_for("auth.index"))
        else:
            return f(*args, **kwargs)
    return decorator
