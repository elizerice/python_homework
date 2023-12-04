for i in range(int(input()[1:])):
    text = input()
    if "#" in text:
        text = text[:text.find("#")]
    print(text)
