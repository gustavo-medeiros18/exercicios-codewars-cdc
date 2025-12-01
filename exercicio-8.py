# Abordagem mostrada na aula
def century(ano):
    parte_inteira = ano // 100
    parte_decimal = ano % 100

    if parte_decimal > 0:
        parte_inteira += 1
    
    return parte_inteira

# Abordagem alternativa: usando uma fórmula direta
# def century(year):
#     return (year + 99) // 100

print(century(2025))
print(century(2000))
print(century(1705))
print(century(1900))
print(century(1601))
print(century(2742))
print(century(70))