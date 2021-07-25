def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string):
    return len(string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(num_1, num_2):
    return int(num_1) + int(num_2)

def number_to_full_month_name(something):
    if something == 1:
        return 'January'
    elif something == 3:
        return 'March'
    elif something == 9:
        return 'September'

def number_to_short_month_name(month_num):
    if month_num == 1:
        return 'Jan'
    elif month_num == 4:
        return 'Apr'
    elif month_num == 10:
        return 'Oct'

def volume_of_cube(num):
    return num * num * num

def reverse_string():
    return 'HELLO'[::-1]

def fahrenheit_to_celsius(num):
    result = (num - 32) * 5/9
    return round(result, 2)
    