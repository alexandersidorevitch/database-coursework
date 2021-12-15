import os


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def filter_py_files(args: tuple):
    base_catalog, _, files_names = args
    return map(
        lambda relative_path: os.path.join(base_catalog, relative_path),
        filter(
            lambda filename: filename.endswith('.py'),
            files_names
        )
    )


def get_file_names():
    return iter(map(filter_py_files, os.walk('shop')))


def write_all_info_from_files(filename) -> None:
    with open(filename, 'w') as write_file:
        for walk in get_file_names():
            for relative_path in walk:
                with open(relative_path, 'r') as read_file:
                    write_file.write(f'File name: {relative_path}' + '\n\n\n')
                    write_file.write(read_file.read() + '\n\n\n')


write_all_info_from_files('1.txt')
