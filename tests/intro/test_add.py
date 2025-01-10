from intro import my_math_functions


def test_add_two_numbers():
    result = my_math_functions.add_two_numbers(5, 10)
    assert 15 == result
