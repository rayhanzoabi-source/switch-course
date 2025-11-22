def is_palindrome(user_input):
    if user_input == user_input[::-1]:
        return "Your input is Palindrome!"
    else:
        return "Not a Palindrome"

def is_lowercase(user_input):
    if user_input.islower():
        return "All characters are lowercase"
    else:
        return "Not all characters are lowercase"

def are_all_digits(user_input):
    if user_input.isdigit():
        return "All characters are digits"
    else:
        return "Not all characters are digits"

def len_check(user_input, threshold):
    if len(user_input) <= threshold:
        return f"The input length ({len(user_input)}) does not exceed the threshold ({threshold})."
    else:
        return f"The input length ({len(user_input)}) exceeds the threshold ({threshold})!"


def is_empty(user_input):
    if len(user_input) == 0:
        return "You have entered an empty string"
    else:
        return "The input is not empty"

def is_invalid_string(user_input, option):
    """Return True if the input is invalid based on menu option."""
    # Empty string always invalid
    if len(user_input) == 0:
        return True
    
    # If the option is NOT digit-checking (option != 3), we require letters
    if option != 3 and not any(char.isalpha() for char in user_input):
        return True
    
    return False 

#Menu

threshold = 6

while True:
    print("\n--- Number Toolbox ---")
    print("1.Check if your input is Palindrome.")
    print("2. Check if all characters in the input string are lowercase.")
    print("3. Verify if all characters in the input are digits.")
    print("4. Check if the length of the input exceeds a predefined threshold.")
    print("5. Check if the input string is empty.")
    print("6. Exit")
    
    try:
        user_choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Please enter a valid number from 1 to 6.")
        continue
    
    if user_choice == 6:
        print("Exiting the program, Thanks")
        break
    if user_choice in [1, 2, 3, 4, 5]:
        user_input = input("Enter your input: ")
        if is_invalid_string(user_input, user_choice):
            print("Invalid input! Please enter a valid string.")
            continue 

    if user_choice == 1:
        print(is_palindrome(user_input))
    
    elif user_choice == 2:
        print(is_lowercase(user_input))
    
    elif user_choice == 3:
        print(are_all_digits(user_input))
    
    elif user_choice == 4:
        user_input = input("Enter your input for length check: ")
        try:
            threshold = int(input("Enter the threshold length: "))
        except ValueError:
            print("Invalid input, using default threshold = 5")
            threshold = 5
        print(len_check(user_input, threshold))
    
    elif user_choice == 5:
        print(is_empty(user_input))
    
    else:
        print("Invalid choice, please try another number.")