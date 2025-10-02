#importing libraries in python
# Math & Numbers
import math
import random
import statistics
from fractions import Fraction
from decimal import Decimal
import cmath

#  Math examples 
print("Square root of 16:", math.sqrt(16))
print("Cosine of 90 degrees:", math.cos(math.radians(90)))
print("Value of pi:", math.pi)

# Random examples 
print("Random integer (1–10):", random.randint(1, 10))

# Statistics examples
data = [10, 20, 30, 40, 50]
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Standard Deviation:", statistics.stdev(data))

# Fractions example
f = Fraction(3, 4) + Fraction(1, 2)
print("Fraction result (3/4 + 1/2):", f)

# Decimal example 
d = Decimal("0.1") + Decimal("0.2")
print("Decimal result (0.1 + 0.2):", d)

# Complex math (cmath) example
z = complex(1, 2)  # 1 + 2j
print("Complex number:", z)

