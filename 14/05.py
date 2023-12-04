a = int(input())
b = int(input())
c = int(input())
def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print('это треугольник')
    else:
        print('это не треугольник')
triangle(a, b, c)
