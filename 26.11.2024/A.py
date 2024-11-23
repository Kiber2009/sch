c: int = 0

while True:
    s: int = int(input())
    if s == 0:
        break
    if s % 3 == 0:
        c += 1

print(c)
