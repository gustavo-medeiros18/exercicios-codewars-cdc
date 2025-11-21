# brute force
def find_smallest_int(arr: list):
    smallest_item = arr[0]
    size = len(arr)

    for i in range(1, size):
        if arr[i] <= smallest_item:
            smallest_item = arr[i]
    
    return smallest_item

# pythonic
def find_smallest_int(arr: list):
    return min(arr)

input_list = [34, 15, 88, 2]
print(find_smallest_int(input_list))

input_list = [34, -345, -1, 100]
print(find_smallest_int(input_list))