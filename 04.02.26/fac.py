n: int = int(input())
s: int = 0
for i in range(1, n + 1):
    r: int = 1
    for j in range(i, 1, -1):
        r *= j
    s += r
print(s)
