from math import gcd, lcm


def c(n1: int, n2: int) -> tuple[int, int]:
    return gcd(n1, n2), lcm(n1, n2)


if __name__ == "__main__":
    i1, i2 = map(int, input("Введите два натуральных числа:\n").split())
    g, l = c(i1, i2)
    print(f"НОД({i1},{i2})={g}")
    print(f"НОК({i1},{i2})={l}")
