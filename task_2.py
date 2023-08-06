'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
'''


def kwargs_to_dict(**keys):
    result = {}
    for key, value in keys.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


print(kwargs_to_dict(day=17, month=12, year=1997,
                     names=['Илья', 'Сергей', 'Жанна'],
                     json={'name': 'Алексей', 'password': 'zxcvb987'}))