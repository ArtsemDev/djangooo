from datetime import datetime, UTC, timedelta

from jose import jwt, JWTError


def create_jwt(payload):
    data = {
        "exp": datetime.now(tz=UTC) + timedelta(days=1),
        "sub": payload
    }
    return jwt.encode(claims=data, key="b65fd02061f8b512e6f70941a03bcd42cf36544f68931cda77329998ef31fb06")


def verify_jwt(token):
    try:
        payload = jwt.decode(token=token, key="b65fd02061f8b512e6f70941a03bcd42cf36544f68931cda77329998ef31fb06")
    except JWTError:
        return {}
    else:
        return payload
