s: int = 0
for i in range(10000, 100000):
    if i % 57 == 0:
        s += i
print(s)  # Answer: 86852895
