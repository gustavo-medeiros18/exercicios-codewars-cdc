# Codigo com os prints para depuração. Dará erro se for
# submetido no CodeWars.
def summation(numero_entrada):
    print("========== INICIO DA FUNCAO ==========")
    print(f"Valor do número de entrada: {numero_entrada}")

    soma = 0
    print(f"Valor da soma após atribuição inicial: {soma}")

    # range(1, 9) -> 1, 2, 3, 4, 5, 6, 7, 8
    for i in range(1, numero_entrada + 1):
        print("---------- INICIO DE UMA RODADA DO for ----------")
        print(f"Valor atual do i: {i}")
        print(f"Valor atual da soma (antes do acúmulo soma + i): {soma}")

        soma = soma + i

        print(f"Valor novo da soma (após o acúmulo soma + i): {soma}")

    return soma

# Codigo sem os prins de depuração.
# def summation(numero_entrada):
#     print("========== INICIO DA FUNCAO ==========")
#     print(f"Valor do número de entrada: {numero_entrada}")

#     soma = 0
#     print(f"Valor da soma após atribuição inicial: {soma}")

#     # range(1, 9) -> 1, 2, 3, 4, 5, 6, 7, 8
#     for i in range(1, numero_entrada + 1):
#         print("---------- INICIO DE UMA RODADA DO for ----------")
#         print(f"Valor atual do i: {i}")
#         print(f"Valor atual da soma (antes do acúmulo soma + i): {soma}")

#         soma = soma + i

#         print(f"Valor novo da soma (após o acúmulo soma + i): {soma}")

#     return soma

print(f"Somatório de 22: {summation(22)}")
