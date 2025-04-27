a = float(input("Zadejte délku strany a: "))
b = float(input("Zadejte délku strany b: "))
c = float(input("Zadejte délku strany c: "))

if a + b > c and a + c > b and b + c > a:
    print("Zadané délky tvoří trojúhelník.")
else:
    print("Zadané délky netvoří trojúhelník.")