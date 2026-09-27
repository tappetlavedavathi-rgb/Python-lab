from functools import wraps
# Global login status
is_logged_in = False
# Access-control decorator
def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in first.")
    return wrapper
# Protected function
@require_login
def view_profile():
    print("Welcome to your profile!")
# Case 1: User is not logged in
print("When logged out:")
is_logged_in = False
view_profile()
# Case 2: User is logged in
print("\nWhen logged in:")
is_logged_in = True
view_profile()
#output:
When logged out:
Access denied. Please log in first.

When logged in:
Welcome to your profile!

