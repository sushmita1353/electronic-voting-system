import os

VOTES_FILE = 'votes.txt'

def store_vote(encrypted_vote):
    with open(VOTES_FILE, 'a') as file:
        file.write(encrypted_vote + '\n')

def read_votes():
    if os.path.exists(VOTES_FILE):
        with open(VOTES_FILE, 'r') as file:
            return file.readlines()
    return []
