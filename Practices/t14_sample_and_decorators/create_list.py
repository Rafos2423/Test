import time


def time_it(func):
    def wrapper(*args, **kwargs):
        try:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Время работы функции {func.__name__}: {end_time - start_time}")
            return result
        except Exception as ex:
            print(f"Работа функции прекращена из-за непредвиденной ошибки: {str(ex)}")
    return wrapper


@time_it
def even_numbers_append(n):
    even_list = []
    for i in range(n + 1):
        if i % 2 == 0:
            even_list.append(i)
    return even_list


@time_it
def even_numbers_comprehension(n):
    even_list = [i for i in range(n + 1) if i % 2 == 0]
    return even_list

print(even_numbers_append(30))
print(even_numbers_comprehension(30))