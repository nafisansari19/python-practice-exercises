def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} hours"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dict):
    #if user_input.isdigit(): #this condition has been commented to show the use of try and except method
    try:
        #user_input_num = int(user_input)
        user_input_num = int(days_and_unit_dict["days"])
        if user_input_num > 0:
            result = days_to_units(user_input_num, days_and_unit_dict["unit"])
            print(result)
        elif user_input_num == 0:
            print("Please enter a number greater than zero")
        else:
            print("you have entered a negative number, please try again!")

    except ValueError:
        print("your input is not a valid number, please provide valid number!")

user_input_message = "enter number of days and conversion unit! \n"