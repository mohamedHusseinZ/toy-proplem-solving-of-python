def convert_to_24_hour(hour, minute, period):
    if period.lower() == "pm" and hour != 12:
        hour += 12
    elif period.lower() == "am" and hour == 12:
        hour = 0

    # to ensure to digits
    hour_string = f"{hour:02}"
    minute_string = f"{minute:02}"

    # to have 4 digits
    time_24_hour = hour_string + minute_string

    return time_24_hour

hour_input = 8
minute_input = 30
period_input = "am"
result = convert_to_24_hour(hour_input, minute_input, period_input)
print(result)
  





def positive_numbers(a, b, c):
    if a > 0:
        return True
    elif b > 0:
        return True
    elif c > 0:
        return True
    else:
        return "False"


result = positive_numbers(0, 3, 5)
print(result)




def solve(r):
    vowels = "aeiou"
    max_value = 0
    current_value = 0

    for char in r:
        if char not in vowels:
            current_value += ord(char) - ord('a') + 1
            # ord is used to get the unicode piont of a given character
        else:
            max_value = max(max_value, current_value)
            current_value = 0

    # Check for the last substring
    max_value = max(max_value, current_value)

    return max_value


print(solve("zodiacs"))  
print(solve("strength"))  









