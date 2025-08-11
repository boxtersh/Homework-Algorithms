import pytest
import main


@pytest.mark.parametrize('lst,start,end,max,i_relative,i_absolute',
                         [([1, 2, 3], 1, 2, 3, 1, 2),
                          ([-1, -2, -3, -7, -5, 0], 4, 5, 0, 1, 5)])
def test_max_in_range_positive_1(lst, start, end, max, i_relative, i_absolute):
    res1, res2, res3 = main.max_in_range(lst, start, end)

    assert res1 == max, f'Ожидалось: {max}, получили: {res1}'
    assert res2 == i_relative, f'Ожидалось: {i_relative}, получили: {res2}'
    assert res3 == i_absolute, f'Ожидалось: {i_absolute}, получили: {res3}'


def test_argument_1_not_list():
    with pytest.raises(AssertionError):
        main.max_in_range(5, 5, 5)


def test_argument_2_not_int():
    with pytest.raises(AssertionError):
        main.max_in_range(5, '5', 5)


def test_argument_3_not_int():
    with pytest.raises(AssertionError):
        main.max_in_range(5, 5, '5')


def test_index_1_is_outside_range_list():
    with pytest.raises(AssertionError):
        main.max_in_range([1, 2, 3], 4, 1)


def test_index_2_is_outside_range_list():
    with pytest.raises(AssertionError):
        main.max_in_range([1, 2, 3], 1, 4)


def test_index_equal():
    with pytest.raises(AssertionError):
        main.max_in_range([1, 2, 3], 2, 2)


def test_start_less_end():
    with pytest.raises(AssertionError):
        main.max_in_range([1, 2, 3], 2, 1)


def test_list_empty():
    with pytest.raises(AssertionError):
        main.max_in_range([], 2, 1)


def test_list_less_2_values():
    with pytest.raises(AssertionError):
        main.max_in_range([7], 2, 1)
