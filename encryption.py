import hashlib

def encrypt_vote(vote):
    return hashlib.sha256(vote.encode()).hexdigest()
