# Interactive Script to Check if Passwords have been Compromised

This tool uses the https://haveibeenpwned.com API to check if given passwords are included in the list of
known compromises.

## Prerequisites
- Install [Python](https://www.python.org/downloads) 3.
- Install required Python packages:

```
pip install -r requirements.txt
```

## Usage

Launch:
```
python check_pwned_passwords.py
```

And enter a password (obfuscated) into the prompt:
```
Password:
```

The tool will continually prompt for passwords until Ctrl-C is entered.

## Notes

* The passwords provided to the tool do not leave the local Python process.
* Only the SHA1 hash (actually the first 5 characters _only_, per the https://haveibeenpwned.com API) of the password 
  is sent to https://haveibeenpwned.com for verification.
