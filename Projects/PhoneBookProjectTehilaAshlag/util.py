
def is_valid_email(email):
    import re
    return re.match(r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,5}$', email)