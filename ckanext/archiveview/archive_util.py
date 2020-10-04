def add_path_to_file_tree(file_tree, dir_path):
    splitted_path = dir_path.split('/')

    path = splitted_path[:-1]
    new_file = splitted_path[-1]

    current_item = file_tree
    for item in path:
        if item not in current_item.keys():
            current_item[item] = {}
        current_item = current_item.get(item)

    if new_file:
        current_item[new_file] = None


def zipfile_to_tree(zipfiles):
    result = {}
    for file in zipfiles:
        add_path_to_file_tree(result, file.filename)
    return result
