#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 13, 2022
# This program asks the user how many numbers they would like
# to add together and then it uses a while loop to ask for the
# number the user wants to add and add it to the current sum.


def main():
    # initialize the loop counter, sum and answer
    loop_counter = 0
    sum = 0
    answer = ""
    
    while True:
        # get user number as string
        user_number_1_string = input("How many numbers would "
                                     "you like to add?: ")
        print("")

        try:
            # convert the first number from string to integer
            user_number_1_int = int(user_number_1_string)

            if user_number_1_int >= 0:
                # calculate the sum of the entered numbers
                while (loop_counter < user_number_1_int):
                    # get input from the user
                    user_number_2_string = input("Enter a whole number: ")

                    try:
                        # convert the entered number from string to integer
                        user_number_2_int = int(user_number_2_string)
                        # joins the strings

                        if user_number_2_int < 0:
                            print("{} cannot be added. Please enter a whole "
                                  "number".format(user_number_2_string))
                            print("")
                            continue
                        print("")
                        print("{} added to the sum.".format(user_number_2_int))
                        print("")
                        sum = sum + user_number_2_int
                        loop_counter = loop_counter + 1
                        answer += str(user_number_2_int) + " + "
                    except Exception:
                        print("{} is not a number."
                              .format(user_number_2_string))
                        print("")
                        continue

                if loop_counter == user_number_1_int:
                    print("{}0 = {} ".format(answer, sum))
                    print("The sum is {}.".format(sum))
                    break
            else:
                print("{} is not a whole number. Enter a whole number."
                      .format(user_number_1_int))
                print("")
        except Exception:
            print("{} is not a number.Please try again."
                  .format(user_number_1_string))
            print("")


if __name__ == "__main__":
    main()
