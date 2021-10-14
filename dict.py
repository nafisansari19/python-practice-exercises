#Allow user to input:
# 1. number of days, e.g. 50
# 2. unit to convert to, e.g. hours
from helper import validate_and_execute, user_input_message

#showing user how while loops works
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dict)
    validate_and_execute(days_and_unit_dict)

