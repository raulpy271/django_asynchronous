from os import scandir


def get_all_files_path(path):
    nodes = scandir(path)
    only_files = filter(lambda node: node.is_file(), nodes)
    only_path_of_files = map(lambda node: node.path, only_files)
    return list(only_path_of_files)


def has_extensions(path, extensions):
    for extension in extensions:
        if path.endswith( '.' + extension):
            return True
    return False


def get_extension(path):
    if '.' in path:
        path_separeted_by_dot = path.split('.')
        extension = path_separeted_by_dot.pop()
        return extension
    else:
        return ''
    

def get_delimiter(path):
    return ','


def catch_parser_error(parser):
    def parser_with_handler_of_error(path):
        try:
            return parser(path)
        except:
            print('Can\'t parse this file: ' + path)
    return parser_with_handler_of_error


