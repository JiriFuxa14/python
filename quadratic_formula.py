import cmath
a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
v1 = (-b-cmath.sqrt(d))/(2*a)
v2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(v1,v2))



