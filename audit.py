import hashlib
from storage import read_votes  # Import the function to read votes from storage

def audit_votes():
    """Audit the votes by displaying them."""
    votes = read_votes()
    print("\nAudit Results:")
    if votes:
        print(f"Total Votes Cast: {len(votes)}")
        for idx, vote in enumerate(votes, start=1):
            print(f"Vote {idx}: {vote.strip()}")
    else:
        print("No votes have been cast yet.")

def count_votes():
    """Count and display the number of votes for each candidate."""
    votes = read_votes()
    results = {"Candidate A": 0, "Candidate B": 0, "Candidate C": 0}
    
    for vote in votes:
        if vote.startswith(hashlib.sha256(b"Candidate A").hexdigest()):
            results["Candidate A"] += 1
        elif vote.startswith(hashlib.sha256(b"Candidate B").hexdigest()):
            results["Candidate B"] += 1
        elif vote.startswith(hashlib.sha256(b"Candidate C").hexdigest()):
            results["Candidate C"] += 1
    
    print("\nElection Results:")
    for candidate, count in results.items():
        print(f"{candidate}: {count} votes")
