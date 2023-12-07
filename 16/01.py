pi = 3.14159
def circle_length(radius: int):
    return 2 * pi * radius
def circle_area(radius: int):
    return pi * radius ** 2
def main():
    print(circle_area(10))

print(circle_length(5))
print(circle_area(10))

