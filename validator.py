import re

def validate_email(email):
    # Use a raw string for the regex
    return bool(re.match(r"^.+@(\[?)[a-zA-Z0-9-.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))
