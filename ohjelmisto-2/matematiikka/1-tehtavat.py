# 1-tehtavat.py
import math
import numpy as np

# 1
print("\nTehtävä 1")
def rad_deg(rad):
    return rad * (180/math.pi) # math ratkaisu

# a)
print(rad_deg(2.493))
# print(np.degrees(2.493)) numpy ratkaisu

# b)
print(rad_deg(0.911))

# 2.
print("\nTehtävä 2")
def deg_rad(deg):
    return deg * (math.pi/180)

# a)
print(deg_rad(137.7))

# b)
print(deg_rad(62.3))

# 3
print("\nTehtävä 3")
for degree in (30, 45, 60, 90, 120, 135, 150, 180, 270, 360):
    print(f"{degree}° = {deg_rad(degree):.3}rad")