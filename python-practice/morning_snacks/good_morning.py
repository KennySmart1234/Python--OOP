
def convert_to_snake_case(text):
    convrted = ""
    for char in text:
        if char.isupper():
            convrted += "_" + char.lower()
        else:
            convrted += char
    return convrted

text = "HelloHorizonArise"
print(convert_to_snake_case(text))



def count_numbers(numbers):

    return "{:,} $".format(numbers)

numbers = 4325678665325797892
print(count_numbers(numbers))




def replace_words_with_ellipsis(text):
    result = ""
    for char in text:
        if char == "Hello":
            result += "_"
            text = text.replace(char, ".")

    return text

word = "Hello world"
print(replace_words_with_ellipsis(word))


import random
import string


def generate_pattern(text):
    result = ""

    for character in text:
        if character == "A":
            result += random.choice(string.ascii_uppercase)
        elif character == "#":
            result += random.choice(string.digits)
        elif character == "@":
            result += random.choice(string.ascii_lowercase)
        else:
            result += character

    return result


text = "AAA-###-@@"
print(generate_pattern(text))
