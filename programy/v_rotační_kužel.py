import math
#sp = obsah podstavy
#r = poloměr
#v = výška
pi = math.pi
r = int(input("Zadej poloměr (cm): "))
v = int(input("Zadej výšku (cm): "))
sp = pi * r**2
V = 1/3  * sp * v
print("Objem kužele je:", round(V), "cm^3")