import string
import random


def generate_password(m):
    symbols = string.ascii_letters + string.digits
    no_symbs = "Ll1iIOo0"
    for symb in no_symbs:
        symbols = symbols.replace(symb, "")
    return "".join(random.sample(symbols, m))


def main(n, m):
    passwords = set()
    while len(passwords) < n:
        passwords.add(generate_password(m))
    return list(passwords)
