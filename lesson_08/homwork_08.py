str1= ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def elem_summ(elements):
    new_list = elements.split(",")
    all_elm_summ = 0
    for elem in new_list:
        try:
            all_elm_summ += int(elem)
        except ValueError:
                return "Cant do it"
    return all_elm_summ

def sum_numbers_in_data_structure(data):
    result = []
    for elem in data:
        result.append(elem_summ(elem))
    return result

print(sum_numbers_in_data_structure(str1))