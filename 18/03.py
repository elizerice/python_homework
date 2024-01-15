def encrypt_caesar(msg, shift):
    encrypted = ""
    for symbol in msg:
        if symbol != ' ':
            if ord(symbol) >= 1072 and ord(symbol) <= 1103:
                char = ord(symbol) + shift
                if char > 1103:
                    char = char - 32
                symbol = chr(char)
            elif ord(symbol) >= 1040 and ord(symbol) <= 1071:
                char = ord(symbol) + shift
                if char > 1071:
                    char = char - 32
                symbol = chr(char)
        encrypted += symbol
    return encrypted


def decrypt_caesar(encrypted, shift):
    decrypted = ""
    for symbol in encrypted:
        if symbol != ' ':
            if ord(symbol) >= 1072 and ord(symbol) <= 1103:
                char = ord(symbol) - shift
                if char < 1072:
                    char = char + 32
                symbol = chr(char)
            elif ord(symbol) >= 1040 and ord(symbol) <= 1071:
                char = ord(symbol) - shift
                if char < 1040:
                    char = char + 32
                symbol = chr(char)
        decrypted += symbol
    return decrypted
