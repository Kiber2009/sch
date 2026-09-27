n: int = 0
for i in range(1000, 10000):
    if sum(map(int, str(i))) % 9 == 0:
        n += 1
print(n)  # Answer: 1000
