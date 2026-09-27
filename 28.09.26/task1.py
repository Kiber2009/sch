s: float = 0
for i in range(5, 101):
    s += i * (i + 2) / ((i + 1) * (i + 3))
print(round(s, 2) * 100) # Answer: 9061
