import string
import random
def generate_password(m):
    symbols = string.ascii_letters + string.digits
    symbols = "".join(symb for symb in symbols if symb not in "Ll1iIOo0")
    return "".join(random.choice(symbols) for _ in range(m))

def main(n, m):
    passwords = list()
    while len(passwords) < n:
        passwords.append(generate_password(m))
    return passwords
