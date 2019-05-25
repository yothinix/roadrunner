from main import fizzbuzz


def test_zero_return_zero():
    expected = 0
    actual = fizzbuzz(0)
    assert actual == expected


def test_one_return_one():
    expected = 1
    actual = fizzbuzz(1)
    assert actual == expected


def test_three_return_fizz():
    expected = "fizz"
    actual = fizzbuzz(3)
    assert actual == expected


def test_five_return_buzz():
    expected = "buzz"
    actual = fizzbuzz(5)
    assert actual == expected


def test_six_return_fizz():
    expected = "fizz"
    actual = fizzbuzz(6)
    assert actual == expected


def test_fiftheen_return_fizzbuzz():
    expected = "fizzbuzz"
    actual = fizzbuzz(15)
    assert actual == expected
