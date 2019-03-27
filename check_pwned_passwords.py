import hashlib
import requests
import getpass
import argparse

PWNED_BASE_URL = 'https://api.pwnedpasswords.com/range'

def is_password_pwned(password):
    h = hashlib.sha1()
    h.update(password)
    hash = h.hexdigest()
    r = requests.get('%s/%s' % (PWNED_BASE_URL, hash[:5]))
    return hash[5:].upper() in r.text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Interactive script to verify whether passwords have been comprised, according to https://haveibeenpwned.com')
    args = parser.parse_args()
    try:
        while True:
            if is_password_pwned(getpass.getpass(prompt='Password: ', stream=None)):
                print 'Password has been pwned...  Change it if you haven\'t already!'
            else:
                print 'Password has not been pwned (as far as we know)'
    except KeyboardInterrupt:
        pass

