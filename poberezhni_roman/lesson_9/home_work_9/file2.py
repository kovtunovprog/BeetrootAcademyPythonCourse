import sys


def print_dir_sys_path():
    import sys
    directories = [*sys.path]
    for i in directories:
        print(f'{i}\n')

def add_dir_in_sys_dirs(adres: str):
    import sys
    sys.path.append(adres)

def is_you_dir_in_sys_path(adres: str):
    import sys
    if sys.path.index(adres) > 0:
        print(f'Your {adres} is in list at number - {sys.path.index(adres)}')

add_dir_in_sys_dirs('/home/alaru/Documents')

print_dir_sys_path()

is_you_dir_in_sys_path('/home/alaru/Documents')