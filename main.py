def fizzbuzz(input):
    if input == 0:
        return input
    if input % 3 == 0 and input % 5 == 0:
        return "fizzbuzz"
    if input % 3 == 0:
        return "fizz"
    if input == 5:
        return "buzz"
    return input
