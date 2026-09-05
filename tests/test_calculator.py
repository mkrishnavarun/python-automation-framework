import pytest


@pytest.mark.parametrize(
    "first_number, second_number, expected_result",
    [
        (1, 2, 3),
        (5, 10, 15),
        (100, 200, 300),
    ]
)
def test_addition(first_number, second_number, expected_result):
    assert first_number + second_number == expected_result