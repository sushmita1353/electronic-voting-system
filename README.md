# Electronic Voting System

## Overview

The Electronic Voting System is designed to facilitate secure and confidential voting. This system includes user authentication, vote casting, vote storage, and auditing mechanisms to ensure the integrity and fairness of the election process.

## Features

- **Confidentiality:** Votes are private and not accessible by other users.
- **Integrity:** Votes cannot be altered once cast.
- **Authentication:** Users must be verified before voting.
- **Auditability:** Provides mechanisms to verify the integrity of the voting process.

## Components

1. **User Authentication:** Handles user verification before voting.
2. **Vote Casting:** Allows users to cast their votes securely.
3. **Vote Storage:** Stores votes in an encrypted format.
4. **Vote Counting:** Counts the number of votes for each candidate.
5. **Results Disclosure:** Displays the results of the election.

## Files

- `auth.py`: Handles user authentication.
- `encryption.py`: Provides functions to encrypt votes.
- `main.py`: Entry point of the system with options to cast votes and view results.
- `storage.py`: Manages reading votes from storage.
- `voting.py`: Manages the voting process.
- `audit.py`: Handles vote auditing and counting.
- `votes.txt`: File used to store encrypted votes.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Sushmita/electronic_voting_system.git
