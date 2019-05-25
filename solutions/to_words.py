# Print numbers in plain words (up to 1000)
#
# For example,
# 1           :       "one"
# 10          :       "ten"
# 13          :       "thirteen"
# 247         :       "two hundred forty seven"

import math

words = {
    0:  "zero",
    1:  "one",
    2:  "two",
    3:  "three",
    4:  "four",
    5:  "five",
    6:  "six",
    7:  "seven",
    8:  "eight",
    9:  "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",

    100: "hundred",
    1_000: "thousand",
    1_000_000: "million",
    1_000_000_000: "billion",
}


def to_words(number):
    if number < 0 or number > 999_999_999_999:
        return "Number should be in range - [0..999,999,999,999]"

    if number in words:
        return [words[number]]

    result = []

    divisor = closest_divisor(number)
    while divisor > 1:
        under_1000, number = divmod(number, divisor)
        result += split_number_under_1000(under_1000)
        result.append(divisor)

        divisor = closest_divisor(number)

    if number != 0:
        result += split_number_under_1000(number)

    return " ".join([words[num] for num in result])


def split_number_under_1000(number):
    if number in words:
        return [number]

    result = []

    hundreds, number = divmod(number, 100)
    if hundreds > 0:
        result.append(hundreds)
        result.append(100)

    if number >= 20:
        tens, number = divmod(number, 10)
        result.append(tens*10)

    if number != 0:
        result.append(number)

    return result


def closest_divisor(number):
    if number > 1_000_000_000:
        return 1_000_000_000
    elif number > 1_000_000:
        return 1_000_000
    elif number > 1_000:
        return 1_000

    return 0


print(to_words(0))
print(to_words(1))
print(to_words(20))
print(to_words(120))
print(to_words(800))
print(to_words(223))
print(to_words(247))
print(to_words(203))
print(to_words(997))
print(to_words(19828))
print(to_words(123_419_828))
print(to_words(123_000_828))
print(to_words(123_000_828_000))
print(to_words(123_000_800_000))
