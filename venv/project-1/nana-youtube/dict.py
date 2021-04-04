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

# to_seconds = 24
# name_of_units = "hours"

# user_input = int(input("Please enter the number of days : \n"))
from modules import validate_and_execute
# from vars import user_input_message
from vars import * as v
import logging

user_input = ""

while user_input != "exit":
    user_input = input(v.user_input_message)
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_units_dict = {"days": days_and_units[0], "units": days_and_units[1]}
    print(days_and_units_dict)
    validate_and_execute(days_and_units_dict)
