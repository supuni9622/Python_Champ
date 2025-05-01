def get_max(number_list):
    max_number = number_list[0]
    for item in number_list:
        if item > max_number:
            max_number = item
    return max_number

def get_min(number_list):
    min_number = number_list[0]
    for item in number_list:
        if item < min_number:
            min_number = item
    return min_number
