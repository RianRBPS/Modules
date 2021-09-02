import math

n = int(input('Need any Help?'
              '\n[1] = Yes'
              '\n[2] = No'
              '\n:'))
if n == 1:
    help(math)

##################################

value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(value))

          # Preferência de números pares ao arredondar
print(round(4.5)) # 4
print(round(5.5)) # 6

#################################

print(math.pi)

from math import pi

print(pi)

       # If I ever need to use one of those, the Numpy module is a must have
print(math.e)
print(math.inf)
print(math.nan)
       ###

print(math.log(math.e))
print(math.log(100, 10))

#################################

print(math.sin(10))
print(math.cos(10))
print(math.tan(10))

#################################

math.degrees(pi/2)
print(math.radians(180))
