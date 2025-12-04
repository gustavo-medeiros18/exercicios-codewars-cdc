def partlist(lista_entrada):
    lista_resultante = []
    tam_lista = len(lista_entrada)
    espaco = " "

    for limite in range(1, tam_lista):
        primeiro_pedaco_sublista = lista_entrada[:limite]
        segundo_pedaco_sublista = lista_entrada[limite:]
        
        primeiro_pedaco_str = espaco.join(primeiro_pedaco_sublista)
        segundo_pedaco_str = espaco.join(segundo_pedaco_sublista)

        tupla = (primeiro_pedaco_str, segundo_pedaco_str)
        lista_resultante.append(tupla)
    
    return lista_resultante

lista_entrada = ["az",  "toto",  "picaro",  "zone",  "kiwi"]
print(partlist(lista_entrada))

lista_entrada = ["Brasil",  "China",  "India",  "Japão"]
print(partlist(lista_entrada))