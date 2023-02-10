numero = input("Ingrese su numero:")
fact = int(numero)
count = 1
count2 = 1
while count2 <= fact:
    count = count * count2
    count2 = count2 + 1
print(count)