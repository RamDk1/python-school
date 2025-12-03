def index_all(search_list, item):
    index_list = []
    for index, value in enumerate(search_list):
        if value == item:
            index_list.append([index])
        elif isinstance(value, list):
            for i in index_all(value, item):
                index_list.append([index] + i)
    return index_list

example_list = [[[1,2,3], 2, [1,3]], [1, 2, 3]]
print(index_all(example_list, 2))
