def invertirStrLista(lista,n=0):
    if n==len(lista):
        return lista
    else:
        lista[n] = lista[n][::-1]
        n += 1
        return invertirStrLista(lista,n)

invertida = ["ingenieria","sistemas","mujeres"]
print(invertirStrLista(invertida))