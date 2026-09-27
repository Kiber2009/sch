s: float = 0
for i in range(1, 104):
    t: float = i * (i + 1) / (i + 2)
    if i % 2 == 0:
        s -= t
    else:
        s += t
print(round(s, 2) * 100)  # Answer: 5140
