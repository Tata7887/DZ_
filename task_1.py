'''
 Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
'''

import os


string = "D:\Tata\python_new\DZ_5\Task_1.py"

#string = "C:/Алексей/Desktop/GreekBrains/ДОМАШКА/Python_advanced/Seminar2/seminar.py"

def func(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

print( {func(string)})
