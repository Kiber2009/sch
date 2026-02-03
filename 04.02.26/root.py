n: int = int(input())
while len(str(n)) != 1:
    s: int = 0
    for i in str(n):
        s += int(i)
    n: int = s
print(n)
