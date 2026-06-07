# Tests for the repeated removal logic.
# We only test removal_order, since get_input and main rely on
# interactive input/output.
from Repeated_Removal import removal_order


# The two official sample cases.
def test_sample_one():
    assert removal_order("546") == ["4", "5", "6"]


def test_sample_two():
    assert removal_order("564") == ["5", "4", "6"]


# A single digit is simply removed on its own.
def test_single_digit():
    assert removal_order("9") == ["9"]


# removal_order also accepts a list of digit strings (as get_input returns).
def test_accepts_list_input():
    assert removal_order(["5", "4", "6"]) == ["4", "5", "6"]


# Already descending: each step the smallest (last) digit is removed first.
def test_descending_number():
    assert removal_order("4321") == ["1", "2", "3", "4"]


# Already ascending: the leading digit is removed first every time.
def test_ascending_number():
    assert removal_order("1234") == ["1", "2", "3", "4"]


# A zero in the middle leaves the largest number when removed first.
def test_number_with_zero():
    assert removal_order("4205") == ["0", "2", "4", "5"]


# Leading zeros are preserved (the number is treated as a string).
def test_leading_zero_preserved():
    assert removal_order("1010") == ["0", "0", "1", "1"]


# The result always contains every original digit exactly once.
def test_all_digits_returned():
    number = "583921"
    order = removal_order(number)
    assert len(order) == len(number)
    assert sorted(order) == sorted(number)


# Run all the tests and report.
def main():
    test_sample_one()
    test_sample_two()
    test_single_digit()
    test_accepts_list_input()
    test_descending_number()
    test_ascending_number()
    test_number_with_zero()
    test_leading_zero_preserved()
    test_all_digits_returned()
    print("All tests passed!")


if __name__ == "__main__":
    main()
