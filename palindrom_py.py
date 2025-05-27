x = input("zadej slovo nebo větu: ")
x = ''.join(char.lower() for char in x if char.isalnum())
x_clean = ''.join(x.lower().split())
if x_clean == x_clean[::-1]:
    print("slovo je palindrom")
else:
    print("slovo není palindrom")