my_file = open("linkwithkey.txt", "r")
data = my_file.read()
data_into_list = data.split("\n")

def remove_search(list):
    new_list = []
    for item in list:
        if item != "search":
            new_list.append(item)
    return new_list


new_list = remove_search(data_into_list)


def save_to_file(list, updated):
    with open(updated, 'w') as f:
        for item in list:
            f.write(item + '\n')



save_to_file(new_list, 'updated_list.txt')


