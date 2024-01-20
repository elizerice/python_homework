import sys
words = [word.strip() for word in sys.stdin]
words.sort()
words_=sorted(words, key=lambda word: sum(ord(symb) - ord('A') + 1 for symb in word.upper()))
[print(word) for word in words_]
