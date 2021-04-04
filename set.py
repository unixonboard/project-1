# my_set={"Jan","Feb","Mar"}
# print(my_set)
# for i in my_set:
#     print(i,end=" ")

#adding removing ,




# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# print("hi")
#
# firstName = "Rahul"
# lastName  = "Singh"
# age = 34
# ssh = 12345
# height = float(6.2)
# weight = "75KG"
#
# print(firstName,lastName,age,ssh,height,weight)

to_seconds = 24
name_of_units = "hours"

# user_input = int(input("Please enter the number of days : \n"))
def days_to_units(number_of_daya):
    return f"{number_of_daya} days are { number_of_daya * to_seconds} {name_of_units}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("00 value not accepted")
        else:
            print("you have enteres a nagative number")

    except ValueError:
        print("Your input is not a valid number")
user_input = ""
while user_input != "exit":
    user_input = input("Please enter a number: \n")
    list_of_days = user_input.split(",")
    # print(type(user_input))
    for num_of_days_element in set(list_of_days):
        # print(type(user_input.split(",")))
        # print(user_input.split(","))
        # print(type(num_of_days_element))
        validate_and_execute()
# my_var = days_to_units(user_input)
# print(my_var)


