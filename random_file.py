import os
import random

def get_random_file(directory_path):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        return None

    # Get a list of files in the directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Check if there are any files in the directory
    if not files:
        return None

    # Choose a random file from the list
    random_file = random.choice(files)

    return random_file


