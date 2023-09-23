def compound(x, y, z):
    final =  x * pow((1 + y / 100), z)
    print(final)

x = int(input("How much are you starting with: "))
y = int(input("Enter a pertencage: "))
z = int(input("How many years: "))
compound(x, y, z)