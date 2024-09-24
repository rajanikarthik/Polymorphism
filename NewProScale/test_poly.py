import pytest
from ScaleUP import Child


def test_right():
    expected = "Its Pallindrome: 30"
    c = Child(40, 'level', 10)
    assert c.palindrome() == expected

def test_right_difage():
    expected = "Its Pallindrome: 35"
    c = Child(60, 'Madam', 25)
    assert c.palindrome() == expected


def test_failure():
    expected = "Its not Pallindrome"
    c = Child(50, 'SAM', 9)
    assert c.palindrome() == expected
