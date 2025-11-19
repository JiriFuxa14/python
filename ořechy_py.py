class Nuts:

    sum_of_weight = 0

    def __init__(self, weight):
        self.weight = weight
        Nuts.sum_of_weight += weight

    def __del__(self):
        Nuts.sum_of_weight -= self.weight

order_1 = Nuts(25)
order_2 = Nuts(35)
order_3 = Nuts(15)
order_4 = Nuts(20)
print(Nuts.sum_of_weight)
del order_2
print(Nuts.sum_of_weight)
