# access_control.py

def audit_log(func):
    """Decorator to log authorization start and completion."""
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

def compute_access_level(control, favorite_artist):
    """Computes access level: control * 3 + len(artist)."""
    return (control * 3) + len(favorite_artist)

@audit_log
def validate_access(level, control):
    """Compares access level against threshold (control * 5)."""
    threshold = control * 5
    if level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"