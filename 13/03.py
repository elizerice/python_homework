symbols = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "tc",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ы": "y",
    "ъ": "",
    "ь": "",
    "э": "e",
    "ю": "iu",
    "я": "ia",
}
text = input()
result = ""
for symbol in text:
    if symbol.lower() not in symbols:
        result += symbols
        continue
    if not symbol.isupper():
        result += symbols[symbol]
    else:
        result += symbols[symbol.lower()].capitalize()
print(result)
