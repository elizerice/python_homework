def month_name(num, lang):
    if lang == "ru":
        month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
        return month[num - 1]

    if lang == "en":
        month = ['january', 'february ', 'march ', 'april', 'may ', 'june ', 'july ', 'august ', 'september', 'october', 'november', 'december ']
        return month[num - 1]


print(month_name(3, "en"))
