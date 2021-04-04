def days_to_units(number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} minutes"
    else:
        return "unsupported Unit"


def validate_and_execute(days_and_units_dict):
    try:
        user_input_number = int(days_and_units_dict["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_units_dict["units"])
            print(calculated_value)
        elif user_input_number == 0:
            print("00 value not accepted")
        else:
            print("you have enteres a nagative number")
    except ValueError:
        print("Your input is not a valid number")
