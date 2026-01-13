from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    parts = 4
    result = split_integer(value, parts)

    assert sum(result) == value and len(result) == parts


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    parts = 2
    assert split_integer(value, parts) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    parts = 1
    assert split_integer(value, parts) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    parts = 6
    result = split_integer(value, parts)

    assert result == sorted(result) and assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    parts = 5
    result = split_integer(value, parts)

    assert (
        len(result) == parts
        and sum(result) == value
        and result == [0, 0, 1, 1, 1]
    )
