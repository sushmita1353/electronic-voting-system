from auth import authenticate_user
from voting import cast_vote
from audit import audit_votes, count_votes

def main():
    print("Welcome to the Secure Electronic Voting System")
    
    if not authenticate_user():
        print("Authentication failed. Please try again.")
        return
    
    cast_vote()

    # Options for auditing and viewing results (usually restricted to admin)
    print("\nOptions:")
    print("1. Audit votes")
    print("2. Count votes")
    print("3. Exit")
    option = input("\nSelect an option: ").strip()

    if option == '1':
        audit_votes()
    elif option == '2':
        count_votes()
    elif option == '3':
        print("Exiting the system.")
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
