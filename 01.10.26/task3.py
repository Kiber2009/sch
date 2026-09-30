s: float = 0
for i in range(2, 102):
    t: float = 1 / i
    if i % 2 == 0:
        s += t
    else:
        s -= t
print(round(s, 2) * 100)
# Answer: 30
