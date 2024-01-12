morse_code = {'a':'.-',
        'b':'-...',
        'c':'-.-.',
        'd':'-..',
        'e':'.',
        'f':'..-.',
        'g':'--.',
        'h':'....',
        'i':'..',
        'j':'.---',
        'k':'-.-',
        'l':'.-..',
        'm':'--',
        'n':'-.',
        'o':'---',
        'p':'.--.',
        'q':'--.-',
        'r':'.-.',
        's':'...',
        't':'-',
        'u':'..-',
        'v':'...-',
        'w':'.--',
        'x':'-..-',
        'y':'-.--',
        'z':'--.',}
phrase = str(input()).lower()
phrase_morse = str()
for i in (phrase):
    if i != ' ':
        phrase_morse += morse_code[i]
    else:
        phrase_morse += ' '
for i in phrase_morse.split():
    print(i)
