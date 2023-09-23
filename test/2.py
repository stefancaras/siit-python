import re


def majority(the_list):
    new_list = [re.findall(f" {str(el)} ", f" {'  '.join(map(str, the_list))} ") for el in set(the_list)]
    max_val = max(len(el) for el in new_list)
    return ', '.join([el[0].strip() for el in filter(lambda x: len(x) == max_val, new_list)])


print(majority([3, 2, 2, 3, 33]))
