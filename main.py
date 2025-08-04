import random
import time
# ************************* Модуль №5. Задание №2 ****************************************
# ************************* Задача №1 ****************************************************
def __check_list(input_data: list)-> None:
    assert isinstance(input_data, list), f'TypeError Ожидался тип данных int, получили {type(input_data)}'


def __check_list_not_empty(input_data: list)-> None:
    assert len(input_data) != [], f'ValueError Ожидался не пустой список, получили {len(input_data)}'


def __check_list_two_or_more_elements(input_data: list) -> None:
    assert len(input_data) >= 2, f'ValueError Ожидался список не менее 2 элементов, получили {len(input_data)}'


def __check_int(input_data: int)-> None:
    assert isinstance(input_data, int), f'TypeError Ожидался тип данных int, получили {type(input_data)}'


def __check_positive_int(input_data: int)-> None:
    assert input_data > 0, f'ValueError Ожидалось положительное число, получили {type(input_data)}'


def __check_index_belongs_list(arr: list[int|float], start: int, end: int)-> None:
    assert len(arr)-1 >= start and len(arr)-1 >= end,\
        f'ValueError Значение индексов должны быть меньше либо равны {len(arr)-1} получили {start,end}'


def __check_start_less_end(start: int, end: int)-> None:
    assert start < end, \
        f'ValueError Значение индекса start должно быть больше end, start={start} end={end}'


def max_in_range(arr: list[int|float], start: int, end:int) -> (float|int, int, int):

    """
    Функция принимает на вход список и два индекса `start` и `end`,
    возвращает максимальный элемент и две координаты (относительную и абсолютную)
    между `start` и `end` включительно.
    - Абсолютная координата - отсчитывается от начала всего массива.
    - Относительная координата - отсчитывается от начала рассматриваемого диапазона.
    Пример:
    arr = [2,3,5,1,6,2,7,3], start = 3, end = 7
    ответ: 7, 6, 3

    :param arr: Массив чисел int, float
    :param start: начало среза включительно
    :param end: конец среза включительно
    :return: Максимальный элемент списка в интервале среза, индекс позиции Абсолютный, Относительный
    """

    __check_list(arr), __check_list_two_or_more_elements(arr), __check_int(start)
    __check_positive_int(start), __check_int(end), __check_positive_int(end)
    __check_index_belongs_list(arr, start, end), __check_start_less_end(start, end)

    max_i = arr[start]

    for i in range(start + 1, end + 1, 1):
        if arr[i] > arr[max_i]: max_i = i

    return arr[max_i], max_i - start, max_i

# Аналитическая сложность алгоритма O(n)= n
# Временная сложность алгоритма О(t) = 2.38 e-06

# ************************* Задача №2 ****************************************************

def rotate_and_reverse(arr: list[int|float], k: int) -> list:
    """
    Функция возвращает новый список, в котором сначала происходит циклический
    сдвиг вправо на k позиций, а затем инверсия всего списка.
    Пример:
    [1,2,3,4,5,6], 2
    ответ: [5,6,1,2,3,4] -> [4,3,2,1,6,5]
    :param arr: Исходный список
    :param k: количество сдвигов
    :return: Реверсивный список после сдвига элементов исходного списка
    """

    __check_list(arr), __check_list_two_or_more_elements(arr)
    __check_int(k), __check_positive_int(k)

    lentght = len(arr)
    buff = arr[lentght - 1]
    new_arr = arr.copy()
    _start = time.time()

    for _ in range(0, k):
        for i in range(lentght):
            new_arr[lentght-1-i] = new_arr[lentght-2-i]

        new_arr[0] = buff
        buff = new_arr[lentght - 1]

    for i in range(lentght//2):
        new_arr[i], new_arr[lentght-1-i] = new_arr[lentght-1-i], new_arr[i]

    print('время=',time.time()-_start)

    return new_arr

# Аналитическая сложность алгоритма O(n)= n^2 + n = O(n)= n^2
# Временная сложность алгоритма О(t) = 5.72 e-06

# ************************* Задача №3 ****************************************************

def reverse_even_elements(arr: list[int|float]) -> list:
    """
    Функция возвращает новый список, в котором только четные числа идут
    в обратном порядке, а нечетные остаются на своих местах.
    Пример:
    [1,2,3,4,5,6,7,8]
    ответ: [1,8,3,6,5,4,7,2]
    :param arr: Исходный список
    :return: Исходный список с четными элементами в обратном порядке
    """

    __check_list(arr)
    _start = time.time()
    new_arr = arr.copy()
    len_arr=len(new_arr)
    list_i_even = [i for i in range(len_arr) if arr[i] % 2 == 0]
    len_even = len(list_i_even)

    for i in range(len_even//2):
        new_arr[list_i_even[i]], new_arr[list_i_even[len_even-1-i]] = new_arr[list_i_even[len_even-1-i]], new_arr[list_i_even[i]]

    print('время=', time.time() - _start)

    return new_arr

# Аналитическая сложность алгоритма O(n)= n
# Временная сложность алгоритма О(t) = 7.87 e-06

# ************************* Задача №4 ****************************************************

def problem_N4(arr: list[int|float]) -> list:
    """
    Массив arr [4,5,6,7] представлен числом 4567
    возвращается массив числа при увеличении его на единицу
    Пример: [4,5,6,7]
    ответ: [4,5,6,8]
    :param arr: Массив числа
    :return: Массив числа + 1
    """

    __check_list(arr)
    _start = time.time()
    len_arr = len(arr)
    revers_a = arr[::-1]
    new_arr = []

    for i in range(len_arr):

        if revers_a[i] + 1 == 10:
            new_arr.append(0)

            if i == len_arr - 1:
                new_arr.append(1)
                #5.7220458984375e-06
                return new_arr[::-1]

        else:
            new_arr.append(revers_a[i] + 1)
            if i == len_arr - 1:
                # 2.002716064453125e-05
                return new_arr[::-1]

            new_arr = new_arr + revers_a[i+1::]
            #4.5299530029296875e-06
            return new_arr[::-1]

# Аналитическая сложность алгоритма O(n)= n
# Временная сложность алгоритма О(t) от 2.00 e-05 до 5.72e-06

