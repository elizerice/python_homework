import string
import random


def generate_password(m):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = uppercase_letters + lowercase_letters + digits
    password = random.choice(uppercase_letters) + random.choice(lowercase_letters) + random.choice(digits)
    while len(password) < m:
        password += random.choice(symbols)
    return ''.join(random.sample(password, m))


def main(n, m):
    passwords = set()
    while len(passwords) < n:
        passwords.add(generate_password(m))
    return list(passwords)
