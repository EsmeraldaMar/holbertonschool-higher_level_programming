#!/usr/bin/python3
def roman_to_int(roman_string):
    # Checks if input is not a string and return 0
    if not isinstance(roman_string, str):
        return 0

    # Define Roman numerals and their corresponding values
    roman_num = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]

    i, result = 0, 0
    while i < len(roman_string):
        match_found = False
        for k, v in roman_num:
            # Checks if current segment of the string matches a Roman numeral
            if roman_string.startswith(k, i):
                result += v  # Add corresponding integer value
                i += len(k)  # Increment index by the length of matched numeral
                match_found = True
                break
        # If no match is found for a segment, return 0
        if not match_found:
            return 0

    return result
