# Método mostrado na aula
def make_negative( number ):
    if number > 0:
        return number * -1
    
    return number

# Método alternativo: usando a função abs
# def make_negative( number ):
    # 1 -> abs: -1
    # -5 -> abs: -5
    # 0 -> abs: -0 -> 0
    # return -abs(number)

print(make_negative(1))
print(make_negative(-5))
print(make_negative(0))
print(make_negative(100))
print(make_negative(-100))
