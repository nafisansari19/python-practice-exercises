cal_to_units = 25
name_of_unit = "hours"


def days_of_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * cal_to_units} {name_of_unit}"


def validate_and_execute():
    #if user_input.isdigit(): #this condition has been commented to show the use of try and except method
    try:
        #user_input_num = int(user_input)
        user_input_num = int(num_of_days_element)
        if user_input_num > 0:
            result = days_of_units(user_input_num)
            print(result)
        elif user_input_num == 0:
            print("Please enter a number greater than zero")
        else:
            print("you have entered a negative number, please try again!")

    except ValueError:
        print("your input is not a valid number, please provide valid number!")

#showing user how while loops works
user_input = ""
while user_input != "exit":
    user_input = input("enter a number as a comma separated list: \n")
    list_of_days = user_input.split(", ")  #here we are coverting user input in to list by using split method

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))
    #showing user how to use for loop and list (enter user input as list rg: [10,15,20,25])
    for num_of_days_element in set(list_of_days):
        validate_and_execute()
