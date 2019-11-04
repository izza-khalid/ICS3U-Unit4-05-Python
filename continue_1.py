#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: October 2019
# This program uses a continue statement


def main():
    # this function uses a continue statement
    sum_of_num = 0

    # input
    loop_counter_string = input("How many numbers would like to add "
                                "together?: ")
    print("")

    # process & output
    try:
        loop_counter = int(loop_counter_string)
        if loop_counter < 0:
            print("Input a positive integer please.")
        else:
            while loop_counter > 0:
                user_input_string = input("Enter a number to add: ")
                try:
                    user_input = int(user_input_string)
                    loop_counter = loop_counter - 1

                    if user_input < 0:
                        continue
                    sum_of_num = sum_of_num + user_input
                except Exception:
                    print("Wrong input. Try again.")
            print("")
            print("Sum of the positive numbers is {}.".format(sum_of_num))
    except Exception:
        print("Wrong input. Try again.")


if __name__ == "__main__":
    main()