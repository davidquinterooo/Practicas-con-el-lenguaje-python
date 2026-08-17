# Algoritmo Quick Sort

def quick_sort(list):
    if len(list) <= 1:
        return list
    
    pivote = list[len(list) // 2]

    menores = [x for x in list if x < pivote]
    iguales = [x for x in list if x == pivote]
    mayores = [x for x in list if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

numeros = [4,9,8,7,6,5,4,3,2,1,0]
lista = quick_sort(numeros)
print(lista)

# Selection Sort Algorithm

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        
        if indice_minimo != i:
            lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

numeros = [64, 25, 12, 22, 11]
print("Lista ordenada:", selection_sort(numeros))