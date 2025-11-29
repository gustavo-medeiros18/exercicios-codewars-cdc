# Abordagem mostrada na aula
def invert(list):
    inverted_list = []

    for item in list:
        inverted_item = item * -1
        inverted_list.append(inverted_item)
    
    return inverted_list

# Abordagem alternativa, usando list comprehension
# def invert(list):
#     inverted_list = [item * -1 for item in list]
#     return inverted_list

input_list = [1, 2, 3, 4, 5]
print(invert(input_list))

input_list = [1, -2, 3, -4, 5]
print(invert(input_list))

input_list = []
print(invert(input_list))