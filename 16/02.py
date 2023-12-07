def discriminant(b,  c, a=1):
    d = b ** 2 - 4 * a * c
    return d


def larger_root(p, q):
    d = discriminant(p, q)
    p = (-p + d ** 1/2 )/ 2
    return p


def smaller_root(p, q):
    d = discriminant(p, q)
    q = (-p - d ** 1 / 2) / 2
    return q


def main():
    print(larger_root(2, 1))


main()
