def b(m: int, n: int) -> tuple[int, int]:
    for i in range(min(m, n), 1, -1):
        if (m % i == 0) and (n % i == 0):
            m //= i
            n //= i
    return m, n


if __name__ == "__main__":
    inp: map[int] = map(int, input("Введите числитель и знаменатель дроби:\n").split())
    print(f"После сокращения: {'/'.join(map(str, b(*inp)))}")
