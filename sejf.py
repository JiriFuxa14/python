# a = vypsat sudý čísla od 1 do 9
# b = vypsat dvouciferný čísla od 20 do 90
# c = přidej čísla od 20 do 90
# d = přidej čísla od 1 do 5
# count = počet cifer
# if = jestli a+b+c+d se nerovná 21 tak pokračuj
# dom. úkol = cifry se nesmí opakovat
count = 0
for a in range(2, 10, 2):
    for b in range (1, 10):
        for c in range (1, 10):
            for d in range (1, 5):
                if a+b+c+d != 21:
                    continue
                print(a, b, c, d, sep="-")
                count += 1
print("pocet cifer:", count)