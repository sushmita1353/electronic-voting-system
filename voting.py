from encryption import encrypt_vote
from storage import store_vote

def cast_vote():
    print("You are about to cast your vote. Please select your preferred candidate:\n")
    print("1. Candidate A")
    print("2. Candidate B")
    print("3. Candidate C")
    
    choice = input("\nEnter the number corresponding to your choice: ").strip()
    
    if choice not in ['1', '2', '3']:
        print("Invalid choice. Please restart the voting process.")
        return
    
    vote = f"Candidate {chr(64 + int(choice))}"  # Converts 1 to 'A', 2 to 'B', etc.
    
    print("\nEncrypting your vote...")
    encrypted_vote = encrypt_vote(vote)
    
    store_vote(encrypted_vote)
    
    print("\nYour vote has been encrypted and stored securely.")
    print("Thank you for voting! Your vote has been successfully cast.")
    print("\nReminder: Your vote is completely anonymous and cannot be traced back to you.")
    print("No one, including system administrators, can access your voting choice.")
    print("Tampering with votes is impossible, ensuring the integrity and fairness of this election.")
