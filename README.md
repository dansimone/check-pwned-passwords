# Interactive Script to Verify whether Passwords have been comprised

This tool uses the https://haveibeenpwned.com API to check if given passwords are included in the list of
known compromises.

## Prerequisites
- Install [Python](https://www.python.org/downloads) 2.7 or later.
- Install required Python packages:

```
pip install -r requirements.txt
```

## Usage

Launch:
```
python check_pwned_passwords.py
```

And enter a password (obfuscating) into the prompt:
```
Password:
```

The tool will continually prompt for passwords until Ctrl-C is entered.

## Notes

* The passwords provided to the tool do not leave the local Python process.
* Only the SHA1 hash (actually the first 5 digits of it _only_, per the https://haveibeenpwned.com API) of the password 
are sent to https://haveibeenpwned.com for verification.