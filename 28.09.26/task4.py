n: int = 0
for i in range(1000, 10000):
    if len(set(str(i))) == 2:
        n += 1
print(n)  # Answer: 567
