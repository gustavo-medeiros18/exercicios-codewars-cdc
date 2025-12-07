# Abordagem mostrada na aula
def difference_in_ages(lista_idades):
    maior = lista_idades[0]
    menor = lista_idades[0]

    for item in lista_idades:
        if item < menor:
            menor = item
        
        if item > maior:
            maior = item
    
    diferenca = maior - menor
    tupla_resultado = (menor, maior, diferenca)

    return tupla_resultado

# Abordagem alternativa, usando as funções
# min e max do Python.
# def difference_in_ages(lista_idades):
#     menor = min(lista_idades)
#     maior = max(lista_idades)
    
#     diferenca = maior - menor

#     return (menor, maior, diferenca)

lista_entrada = [57, 81, 14, 7, 32, 99]
print(difference_in_ages(lista_entrada))

lista_entrada = [16, 22, 31, 44, 3, 38, 27, 41, 88]
print(difference_in_ages(lista_entrada))

lista_entrada = [33, 33, 33]
print(difference_in_ages(lista_entrada))