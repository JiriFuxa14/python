class School:

    num_of_boys = 0
    num_of_girls = 0
    total_number = 0

    def __init__(self, name, m, f):
        self.class_name = name
        self.boys = m
        self.girls = f
        School.num_of_boys += self.boys
        School.num_of_girls += self.girls
        School.total_number = School.num_of_boys + School.num_of_girls

    def __del__(self):
        School.num_of_boys -= self.boys
        School.num_of_girls -= self.girls
        School.total_number -= self.boys + self.girls

trida_1A = School("1.A", 12, 15)
print(School.num_of_boys)

