from convert import convert_to_int


def calculate_sum(first_number, second_number):
    '''
        Given two numbers, converts the numbers to int and return the sum of them.
    '''
    
    first_number = convert_to_int(first_number)
    second_number = convert_to_int(second_number)

    return first_number + second_number