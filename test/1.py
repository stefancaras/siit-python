def split_list(the_list, param):
    if param > len(the_list):
        return "Argumentul e mai mare decât lista."
    return the_list[len(the_list) - param:] + the_list[:len(the_list) - param]


print(split_list([1, 2, 3, 4, 5, 6, 7], 2))
