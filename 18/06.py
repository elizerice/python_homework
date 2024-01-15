def solve(*coefficients):
    coefficients = list(coefficients)
    a,b,c = coefficients[::]
    if len(coefficients) == 3:
        discriminant = b ** 2 - 4 * a * c
        x1 = (-b + discriminant ** 0.5) / (a * 2)
        x2 = (-b - discriminant ** 0.5) / (a * 2)
        return x1, x2
    elif len(coefficients) == 2:
        return - b / (2 *a)
    elif len(coefficients) == 1:
        return 0
    else:
        return "None"
