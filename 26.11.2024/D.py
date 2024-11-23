m: int = 0

while True:
    s: int = int(input())
    if s == 0:
        break
    if s >= m and s % 2 == 0:
        m = s

print(m)
