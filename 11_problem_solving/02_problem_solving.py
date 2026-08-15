import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE
"""
Write a function that takes a list of triangles.
Each triangle is represented as a list e.g. [10, 12, 22] where the three
numbers are the sides of the triangle.
The function should return the count of triangles that are valid.
To be a valid triangle, the sum of any two sides must be larger than the
remaining side

valid_triangles([]) returns 0
valid_triangles([[5, 10, 25]]) returns 0
valid_triangles([[5, 4, 5]]) returns 1

"""


def valid_triangles(triangles):
    valid = 0
    for triangle in triangles:
        triangle_size = sum(triangle)
        if all(triangle_size - side > side for side in triangle):
            valid += 1
    return valid




@run_test
def test_valid_triangles_returns_0_when_passed_no_triangles():
    assert valid_triangles([]) == 0, format_err_msg(0, valid_triangles([]))


@run_test
def test_valid_triangles_returns_0_when_passed_a_list_with_no_valid_triangles():
    assert valid_triangles([[5, 10, 25]]) == 0, format_err_msg(
        0, valid_triangles([[5, 10, 25]])
    )


@run_test
def test_valid_triangles_returns_1_when_passed_a_list_with_a_single_valid_triangle():
    assert valid_triangles([[5, 4, 5]]) == 1, format_err_msg(
        1, valid_triangles([[5, 4, 5]])
    )


@run_test
def test_valid_triangles_returns_2_when_passed_a_list_with_2_valid_and_1_invalid_triangle():
    assert (
        valid_triangles([[5, 10, 25], [5, 4, 5], [542, 586, 419]]) == 2
    ), format_err_msg(
        2, valid_triangles([[5, 10, 25], [5, 4, 5], [542, 586, 419]])
    )


"""
Write a function that takes a list of names.
The function should return a list containing the names of the people who aren't spies.
Recent intelligence has revealed that all spies codenames include the letters 's', 'p' or 'y'.
You can't afford to take any chances, and all names that include those letters should be removed.

counter_spy(['Simon']) returns []
counter_spy(['Simon', 'Poonam', 'Danika']) returns ['Danika']

EXTRA CREDIT:

Also, our spy admin team have asked that the names come back in alphabetical
order, for spy filing purposes.
So if you could do that you'd really be saving them a lot of work. Thanks.

"""


def counter_spy(people):
    innocent = []
    bad_chars = 'SsPpYy'
    for person in people:
        if all(char not in bad_chars for char in person):
            innocent.append(person)
    innocent.sort()
    return innocent


@run_test
def test_counter_spy_returns_an_empty_list_if_the_only_person_is_a_spy():
    assert counter_spy(["Simon"]) == [], format_err_msg(
        [], counter_spy(["Simon"])
    )


@run_test
def test_counter_spy_returns_a_list_with_all_spies_removed():
    assert counter_spy(["Simon", "Cat", "Kyle"]) == ["Cat"], format_err_msg(
        ["Cat"], counter_spy(["Simon", "Cat", "Kyle"])
    )
    assert counter_spy(["Simon", "Alex", "Kyle", "Cat", "Chon", "Danika"]) == [
        "Alex",
        "Cat",
        "Chon",
        "Danika",
    ], format_err_msg(
        ["Alex", "Cat", "Chon", "Danika"],
        counter_spy(["Simon", "Alex", "Kyle", "Cat", "Chon", "Danika"]),
    )


@run_test
def test_counter_spy_returns_a_list_with_names_in_alphabetical_order():
    assert counter_spy(["Simon", "Cat", "Kyle", "Danika", "Alex", "Chon"]) == [
        "Alex",
        "Cat",
        "Chon",
        "Danika",
    ], format_err_msg(
        ["Alex", "Cat", "Chon", "Danika"],
        counter_spy(["Simon", "Cat", "Kyle", "Danika", "Alex", "Chon"]),
    )


"""
This function should take a string representing a time with hours and minutes separated by a colon e.g. "13:25"
Some of the times are written in the 24-hour clock format
This function should return the time written in the 12-hour clock format

"""


def convert_time_string(sample_string):
    time_conversion = {
        '13': '01',
        '14': '02',
        '15': '03',
        '16': '04',
        '17': '05',
        '18': '06',
        '19': '07',
        '20': '08',
        '21': '09',
        '22': '10',
        '23': '11',
        '00': '12'
    }
    if int(sample_string[:2]) > 0 and int(sample_string[:2]) < 13:
        return sample_string
    else:
        return f'{time_conversion[sample_string[:2]]}:{sample_string[-2:]}'


@run_test
def test_convert_time_string_returns_the_string_unchanged_if_already_within_the_right_format():
    assert convert_time_string("06:28") == "06:28", format_err_msg(
        "06:28", convert_time_string("06:28")
    )


@run_test
def test_convert_time_string_converts_an_afternoon_time_to_the_12_hour_format():
    assert convert_time_string("16:07") == "04:07", format_err_msg(
        "04:07", convert_time_string("16:07")
    )


@run_test
def test_convert_time_string_converts_times_in_the_hour_after_midnight_to_the_12_hour_format():
    assert convert_time_string("00:56") == "12:56", format_err_msg(
        "12:56", convert_time_string("00:56")
    )
    assert convert_time_string("00:00") == "12:00", format_err_msg(
        "12:00", convert_time_string("00:00")
    )


"""
This function takes a list of words and returns a list containing only
the palindromes.
A palindrome is a word that is spelled the same way backwards.
E.g. ['foo', 'racecar', 'pineapple', 'porcupine', 'tacocat'] =>
['racecar', 'tacocat']

get_palindromes(["pineapple", "pony"]) returns []
get_palindromes(["pineapple", "pony", "racecar"]) returns ["racecar"]

"""


def get_palindromes(word_list):
    palindromes = [word for word in word_list if word[::-1] == word]
    return palindromes



@run_test
def test_get_palindromes_returns_empty_list_when_passed_empty_list():
    assert get_palindromes([]) == [], format_err_msg([], get_palindromes([]))


@run_test
def test_get_palindromes_identifies_palindromes():
    assert get_palindromes(["racecar"]) == ["racecar"], format_err_msg(
        ["racecar"], get_palindromes(["racecar"])
    )
    assert get_palindromes(["racecar", "racecar"]) == [
        "racecar",
        "racecar",
    ], format_err_msg(
        ["racecar", "racecar"], get_palindromes(["racecar", "racecar"])
    )


@run_test
def test_get_palindromes_ignores_non_palindromes():
    assert get_palindromes(["racecar", "kayak", "tacocat"]) == [
        "racecar",
        "kayak",
        "tacocat",
    ], format_err_msg(
        ["racecar", "kayak", "tacocat"],
        get_palindromes(["racecar", "kayak", "tacocat"]),
    )
    assert get_palindromes(["pineapple", "pony", "racecar"]) == [
        "racecar"
    ], format_err_msg(
        ["pineapple", "pony", "racecar"], get_palindromes(["racecar"])
    )


@run_test
def test_get_palindromes_returns_empty_list_when_passed_no_palindromes():
    assert (
        get_palindromes(["pineapple", "watermelon", "pony"]) == []
    ), format_err_msg([], get_palindromes(["pineapple", "watermelon", "pony"]))


if __name__ == "__main__":
    test_valid_triangles_returns_0_when_passed_no_triangles()
    test_valid_triangles_returns_0_when_passed_a_list_with_no_valid_triangles()
    test_valid_triangles_returns_1_when_passed_a_list_with_a_single_valid_triangle()
    test_valid_triangles_returns_2_when_passed_a_list_with_2_valid_and_1_invalid_triangle()
    test_counter_spy_returns_an_empty_list_if_the_only_person_is_a_spy()
    test_counter_spy_returns_a_list_with_all_spies_removed()
    test_counter_spy_returns_a_list_with_names_in_alphabetical_order()
    test_convert_time_string_returns_the_string_unchanged_if_already_within_the_right_format()
    test_convert_time_string_converts_an_afternoon_time_to_the_12_hour_format()
    test_convert_time_string_converts_times_in_the_hour_after_midnight_to_the_12_hour_format()
    test_convert_time_string_returns_the_string_unchanged_if_already_within_the_right_format()
    test_convert_time_string_converts_an_afternoon_time_to_the_12_hour_format()
    test_convert_time_string_converts_times_in_the_hour_after_midnight_to_the_12_hour_format()
    test_get_palindromes_returns_empty_list_when_passed_empty_list()
    test_get_palindromes_identifies_palindromes()
    test_get_palindromes_ignores_non_palindromes()
    test_get_palindromes_returns_empty_list_when_passed_no_palindromes()
