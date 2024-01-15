translated_text = None
def translate(text):
    global translated_text
    remove_symb = ["у", "е", "ы", "а", "о", "э", "я", "и", "ю", "ё"]
    translated_text = ""

    text_copy = list(translated_text.lower())
    for phrase in text:
        if phrase.lower() not in remove_symb:
            translated_text += phrase
    print(translated_text)
