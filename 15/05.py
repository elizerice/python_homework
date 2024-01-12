def number_in_english(number):
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    tens = [ "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundred = "hundred"

    if 0 <= number <= 9:
        return units[number]
    elif 10 <= number <= 19:
        return teens[number - 10]
    elif number // 100 != 0:
        if number % 100 == 0:
            return units[number // 100] + " " + hundred
        else:
            if 10 <= number % 100 <= 19:
                return units[number // 100] + " " + hundred + " and " + teens[number % 100 - 10]
            else:
                if number % 10 == 0:
                    return units[number // 100] + " " + hundred + " and " + tens[(number // 10) % 10 - 2]
                else:
                    return units[number // 100] + " " + hundred + " and " + tens[(number // 10) % 10 - 2] + " " + units[number % 10]
    else:
        if number % 10 == 0:
            return tens[number // 10 - 2]
        else:
            return tens[number // 10 - 2] + " " + units[number % 10]

print(number_in_english(1).lower())
