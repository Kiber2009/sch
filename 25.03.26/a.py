def a(n1: int | float, n2: int | float, n3: int | float) -> tuple[int | float, int | float, int | float]:
    n1, n2, n3 = sorted((n1, n2, n3))
    return n1, n2, n3


if __name__ == '__main__':
    print(*a(*map(int, input("Введите три натуральных числа:\n").split())))
