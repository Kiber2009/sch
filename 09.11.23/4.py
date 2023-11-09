from random import randint
n = [randint(0, 2) for _ in range(100)]
print(f'Орёл: {n.count(0)}\nРешка: {n.count(1)}')
