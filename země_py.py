## Objem a povrch Země
V = (4/3) * (3.14 * 6378**3)
S = (4 * 3.14) * (6378**2)
print ("Objem Země =" , V , "km3")
print ("Povrch Země =" , S , "km2")

## Kolikrát se Země vejde do Slunce
## Vzorec: V = 4/3 * 3.14 * r**3
poloměr_země = 6378
poloměr_slunce = 696340
kolikrát = poloměr_slunce / poloměr_země
kolikrát = kolikrát**3
print("Země se vejde do slunce",kolikrát,"krát")

##Kolik zemí je potřeba jako korálky po obvodu Slunce?
průměr_země = 12742
průměr_slunce = 1392000
kolik = průměr_slunce / průměr_země
print(round(kolik), "zemí je potřeba.")