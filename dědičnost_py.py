class Polygon:

    #definujeme strany
    def __init__(self, sides):

        self.__sides = sides

    #funce pro získání počtu stran
    def getSides(self):
        return self.__sides

    #funkce pro získání počtu stran ve stringu (definovat string sebe)
    def __str__(self):
        return "Tento n-úhelník má " + str(self.__sides) + " stran. "

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

class Hexagon(Polygon):
    def __init__(self):
        Polygon.__init__(self, 6)

    def __str__(self):
        return super().__str__() + "Toto je šestiúhelník. "

class Octagon(Polygon):
    def __init__(self):
        Polygon.__init__(self, 8)

    def __str__(self):
        return super().__str__() + "Toto je osmiúhelník. "

pentagon = Polygon(5)
print(pentagon)  

hexagon_instance = Hexagon()
print(hexagon_instance)

triangle = Triangle()
print(triangle.getSides())

octagon = Octagon()
print(octagon)