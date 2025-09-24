#mocnina a odmocnina
import math
def umocni(a,n):
    return a**n
print(umocni(4,2))

def odmocni(x, y):
    return x**(1/y)
print(odmocni(16, 2))

#suma hodnot
def sumOf(*args):
    return sum(args)

print(sumOf(5, 7, 8, 2, 11, 9, -25))

#vizitka
def vizitka(**k):
    print("jméno", k["jmeno"])
    print("příjmení", k["prijmeni"])
    print("věk", k["vek"])
    print("pohlaví", k["pohlavi"])

vizitka(jmeno= "Adam", prijmeni= "Sandler", vek= 59, pohlavi= "muž")
vizitka(pohlavi= "bohyně", prijmeni= "Gadot", jmeno= "Gal", vek= 39)

#úkol
def player(*args, **kwargs):
    print("jmeno:", kwargs["jmeno"])
    print("prijmeni:", kwargs["prijmeni"])
    print("Suma:", sum(args))

player(1000, 50000, 72000, 310000, jmeno="Tomáš", prijmeni="Enge", ranking=1)



