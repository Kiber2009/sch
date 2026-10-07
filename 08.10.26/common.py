def base(n: int, b: int) -> str:
    res: str = ""

    while n >= b:
        n, n1 = divmod(n, b)
        res += str(n1)

    return str(n) + res[::-1]
