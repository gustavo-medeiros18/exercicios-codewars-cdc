def count_sheeps(sheep):
    count = 0

    for item in sheep:
        if item == True:
            count += 1
    
    return count

# Maneira alternativa: usando a função (método) count
# def count_sheeps(sheep):
#     count = sheep.count(True)
#     return count

input_list = [
    True,  True,  True,  False,
    True,  True,  True,  True ,
    True,  False, True,  False,
    True,  False, False, True ,
    True,  True,  True,  True ,
    False, False, True,  True
]

print(count_sheeps(input_list))

input_list = [
    True,  False,  False,  False,
    True,  True,  True,  True ,
    True,  False, True,  False,
    True,  False, False, True ,
    True,  True,  True,  True ,
    False, False, True,  True
]

print(count_sheeps(input_list))

input_list = [
    True,  True,  True,  True,
    True,  True,  True,  True ,
    True,  True, True,  True,
    True,  True, True, True ,
    True,  True,  True,  True ,
    True, True, True,  True
]

print(count_sheeps(input_list))