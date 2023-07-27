# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, 
# а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление. 
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}


def reverse_dict(**kwargs):
    result = {}
    for key,value in kwargs.items():
        try: 
            hash(value)
            result[value] = key
        except:
             result[str(value)] = key
    return result



print(reverse_dict(res=1, reverse=[1, 2, 3]))
print(reverse_dict(res='3434', reverse='434'))
