my_file = open("updated_list (copy).txt", "r")
data = my_file.read()
data_into_list = data.split("\n")




only_links = [data_into_list[index] for index in filter(lambda x: x % 2 == 1, range(len(data_into_list)))]
#print(only_links)



def save_to_file(list, updated):
    with open(updated, 'w') as f:
        for item in list:
            f.write(item + '\n')



save_to_file(only_links, 'onlylink_list.txt')

