from math import factorial

from common import base


s: str = base(factorial(57), 7)
print(len(s) - len(s.rstrip("0")))
# Answer: 9
