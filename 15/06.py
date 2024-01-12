def print_document(phrases):
    for phrase in phrases:
        if "секретно" not in phrase.lower():
            print(phrase)

print_document(["Обычная страница", "И еще страница", "Секретно Вот этот вот текст не показывать", "Никому", "Никогда"])
print_document(["Пустой трёп", "который", "никому не интересен"])
