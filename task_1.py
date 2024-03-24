# Напишите функцию, которая принимает на вход строку - абсолютный путь
# до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла,
# расширение файла.

strk = 'https://img3.fonwall.ru/o/ff/cat-standing-majestic-muzzle.jpeg'


def my_func(s):
    *path, a = s.split('/')
    name, extension = a.split('.')
    str_split = ('/'.join(path), name, extension)
    return str_split


print(my_func(strk))
