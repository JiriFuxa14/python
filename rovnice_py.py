
def equation():
    a = float(input("zadej a:"))
    b = float(input("zadej b:"))
    if not isinstance(a, float) or not isinstance(b, float):
        print("Zadej reálné číslo")
        return None
    if a == 0:
        print("A se nesmí rovnat 0")
        return None
    x = -b / a
    l_rovnice = a * x + b
    is_zero = (l_rovnice == 0)
    return l_rovnice

result = equation()
if result is not None:
    print(result)
