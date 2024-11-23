c: int = 0

while True:
    s: str = input()
    if s == "0":
        break
    if s[-1] == "3" and len(s) == 2:
        c += 1

print(c)
