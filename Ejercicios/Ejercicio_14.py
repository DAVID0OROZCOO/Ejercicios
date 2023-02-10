Lista = [1, 2, 3, 4, 55, 6, 7]
SumarLista = sum(Lista)
print(f"La suma de nuestra lista es: {SumarLista}")

def total_elements(Lista):
    count = 0
    for element in Lista:
        count += 1
    return count

print("El total de elementos de la lista es: ", total_elements(Lista))

MediaAritmetica = (SumarLista / total_elements(Lista))
print(f"El resultado de la media aritmetica es: {MediaAritmetica}")