import random
print("This program will generate a strong password with upper/lower cases, numbers and special symbols!\n")
while True:
    while True:
        try:
            length = int(input("Insert the length: "))
        except ValueError:  # ValueError is the exception thrown when an int is expected, but we input something else
            print("\nThe length should be an int, try again\n")
        break
    try:
        if length < 12 or length > 48:
            print("Invalid length, should be > 12 and < 48\n")
            break
    except NameError:  # NameError is the exception thrown when no int has been provided, so the variable length has not been created
        break
    # Create a list with all the character that I want into the password
    choiceList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?']
    password = random.choices(choiceList, k=length) # to choose a random number of list's elements
    passwordString = ''.join(str(element) for element in password)  # join is used to convert directly a list of string into a string, when there are other data type we have to convert into string before executing the join
    print("Your password is: " + passwordString)
    try:
        newPassword = input("Do you want to generate a new password? y/n")
    except newPassword in ['y', 'Y', 'yes', 'YES', 'n', 'N', 'no', 'NO']:
        print("Invalid choice, try again\n")
    if newPassword in ['y', 'Y', 'yes', 'YES']:
        continue
    else:
        break
