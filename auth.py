import getpass

def authenticate_user():
    voter_id = getpass.getpass("Please enter your voter ID: ")
    # Simple check for non-empty ID; replace with real authentication logic
    if voter_id.strip() != "":
        return True
    else:
        return False
