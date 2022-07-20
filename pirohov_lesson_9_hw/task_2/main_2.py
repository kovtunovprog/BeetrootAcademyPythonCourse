import sys


def show_all_pathes():
    for i in sys.path:
        print(i)


def add_new_path(*path: str) -> list:
    for i in path:
        sys.path.append(i)

# test pathes ('D:\Downloads', 'E:\\')


while True:
    action = input('Show all pathes (1), Add new path (2), Quit (q)\n')
    if action == '1':
        show_all_pathes()
    elif action == '2':
        new_path = input('Please enter new path:\n')
        add_new_path(new_path)

    elif action == 'q':
        print('Shutting down...')
        break
    else:
        print('Please do correct input!\n')

