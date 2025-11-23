# Usando if "padrão"
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    
    return "Odd"

#Usando if "compacto"
# def even_or_odd(number):
#     return "Even" if number % 2 == 0 else "Odd"

print(even_or_odd(1))
print(even_or_odd(2))
print(even_or_odd(3))
print(even_or_odd(0))
print(even_or_odd(-2))