# pythonic version
def find_needle(haystack):
    found_position = haystack.index("needle")
    return f"found the needle at position {found_position}"

# brute force version
def find_needle(haystack):
    position = 0

    for item in haystack:
        if item == "needle":
            break
        position = position + 1
    
    return f"found the needle at position {position}"

input_list = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
