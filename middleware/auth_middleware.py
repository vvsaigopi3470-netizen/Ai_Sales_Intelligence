from functools import wraps

from flask import session
from flask import redirect

def admin_required(f):

    @wraps(f)

    def decorated(*args, **kwargs):

        if session.get(
            "role"
        ) != "Admin":

            return redirect(
                "/dashboard"
            )

        return f(
            *args,
            **kwargs
        )

    return decorated