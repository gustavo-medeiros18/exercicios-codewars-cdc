# Abordagem mostrada na aula
def find_needle(haystack):
    position = 0

    for element in haystack:
        if element == "needle":
            break
        
        position += 1

    return f"found the needle at position {position}"

# Abordagem alternativa, usando a função/método index
# def find_needle(haystack):
#     position = haystack.index("needle")
#     return f"found the needle at position {position}"

input_list = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
print(find_needle(input_list))

input_list = ["needle", "junk", "hay", "hay", "moreJunk", "hay", "randomJunk"]
print(find_needle(input_list))

input_list = ["hay", "junk", "hay", "hay", "moreJunk", "hay", "needle"]
print(find_needle(input_list))
