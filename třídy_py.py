class Dog:

    count = 21

    def __init__(self, race, weight, sex, age):
        self.race = race
        self.weight = weight
        self.sex = sex
        self.age = age
        Dog.count += 1

print(Dog.count)

shiba_inu = Dog("Shiba Inu", 10, "M", 1)
shi_tzu = Dog("Shi Tzu", 3, "F", 2 )

print(Dog.count)

maltezacek = Dog("Maltezácký psík", 3, "F", 3)

print(Dog.count)

del maltezacek

print(Dog.count)

