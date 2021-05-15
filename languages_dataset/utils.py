from os import scandir


def get_all_files_path(path):
    nodes = scandir(path)
    only_files = filter(lambda node: node.is_file(), nodes)
    only_path_of_files = map(lambda node: node.path, only_files)
    return list(only_path_of_files)


