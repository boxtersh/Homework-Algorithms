def __check_list(input_data: list) -> None:
    assert isinstance(input_data, list), f'TypeError Ожидался тип данных int, получили {type(input_data)}'


def __check_list_not_empty(input_data: list) -> None:
    assert len(input_data) != [], f'ValueError Ожидался не пустой список, получили {len(input_data)}'


def __check_list_two_or_more_elements(input_data: list) -> None:
    assert len(input_data) >= 2, f'ValueError Ожидался список не менее 2 элементов, получили {len(input_data)}'


def __check_int(input_data: int) -> None:
    assert isinstance(input_data, int), f'TypeError Ожидался тип данных int, получили {type(input_data)}'


def __check_positive_int(input_data: int) -> None:
    assert input_data > 0, f'ValueError Ожидалось положительное число, получили {type(input_data)}'


def __check_index_belongs_list(arr: list[int | float], start: int, end: int) -> None:
    assert len(arr) - 1 >= start and len(arr) - 1 >= end, \
        f'ValueError Значение индексов должны быть меньше либо равны {len(arr) - 1} получили {start, end}'


def __check_start_less_end(start: int, end: int) -> None:
    assert start < end, \
        f'ValueError Значение индекса start должно быть больше end, start={start} end={end}'
