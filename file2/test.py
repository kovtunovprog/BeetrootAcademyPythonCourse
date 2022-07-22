import sys
print(sys.path)
#Якщо хочемо змінити PYTHONPATH, додавши файл, в якому PyCharm шукатиме модуль, в кінці, використовуємо append('smth')
sys.path.append('C:\\Users\\Admin\\Lesson8Homework\\file2')
print(sys.path)
#Якщо хочемо змінити шлях пошуку на іншій поизції, використовуємо insert(index, 'smth')
sys.path.insert(0, 'C:\\Users\\Admin\\Lesson8Homework\\file1')
print(sys.path)