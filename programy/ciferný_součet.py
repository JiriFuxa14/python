def ciferny_soucet():
    x = str(input)
    type(x) == int
    x = int(input("Vlož číslo: "))
    total = sum(int(digit) for digit in str(x))
    print(total)
ciferny_soucet()
