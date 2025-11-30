# Abordagem mostrada na aula
def find_smallest_int(lista):
    menor = lista[0]

    for item in lista:
        if item < menor:
            menor = item
    
    return menor

# Abordagem alternativa: usando a função min()
# def find_smallest_int(lista):
#     return min(lista)

lista_entrada = [34, 15, -88, 2, 10]
print(find_smallest_int(lista_entrada))

lista_entrada = [34, 15, 88, 2]
print(find_smallest_int(lista_entrada))

lista_entrada = [34, -345, -1, 100]
print(find_smallest_int(lista_entrada))
