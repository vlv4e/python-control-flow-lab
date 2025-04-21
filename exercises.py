# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Prompt the user to enter a letter
    letter = input("Enter a letter (a-z or A-Z): ").strip()

    # Check if the input is a single alphabetical character
    if len(letter) == 1 and letter.isalpha():
        # Convert the letter to lowercase for uniformity
        letter_lower = letter.lower()
        
        # Check if the letter is a vowel
        if letter_lower in 'aeiou':
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid entry. Please enter a single letter.")

# Call the function
check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Set the minimum voting age
    voting_age = 18
    
    # Prompt the user to input their age
    age_input = input("Please enter your age: ")
    
    try:
        # Convert the input to an integer
        age = int(age_input)
        
        # Check if the age is valid (non-negative)
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        else:
            # Determine if the user is eligible to vote
            if age >= voting_age:
                print("You are eligible to vote.")
            else:
                print("You are not eligible to vote.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for your age.")

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Prompt the user to input the dog's age
    dog_age_input = input("Input a dog's age: ")
    
    try:
        # Convert the input to an integer
        dog_age = int(dog_age_input)
        
        # Calculate the dog's age in dog years
        if dog_age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        elif dog_age <= 2:
            dog_years = dog_age * 10  # First two years count as 10 dog years each
        else:
            dog_years = 20 + (dog_age - 2) * 7  # First two years + subsequent years

        # Print the calculated age in dog years
        print(f"The dog's age in dog years is {dog_years}.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the dog's age.")

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Prompt the user to enter if it is cold
    is_cold = input("Is it cold? (yes/no): ").strip().lower()
    # Prompt the user to enter if it is raining
    is_raining = input("Is it raining? (yes/no): ").strip().lower()
    
    # Check the conditions and provide clothing advice
    if is_cold == 'yes' and is_raining == 'yes':
        print("Wear a waterproof coat.")
    elif is_cold == 'yes' and is_raining == 'no':
        print("Wear a warm coat.")
    elif is_cold == 'no' and is_raining == 'yes':
        print("Carry an umbrella.")
    elif is_cold == 'no' and is_raining == 'no':
        print("Wear light clothing.")
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")

# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Prompt the user to enter the month
    month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
    # Prompt the user to enter the day of the month
    day_input = input("Enter the day of the month: ")
    
    try:
        # Convert the day input to an integer
        day = int(day_input)
        
        # Validate the day input
        if day < 1 or day > 31:
            print("Invalid day. Please enter a valid day of the month.")
            return
        
        # Determine the season based on the month and day
        if (month == 'December' and day >= 21) or (month == 'January') or (month == 'February') or (month == 'March' and day < 20):
            season = "Winter"
        elif (month == 'March' and day >= 20) or (month == 'April') or (month == 'May') or (month == 'June' and day < 21):
            season = "Spring"
        elif (month == 'June' and day >= 21) or (month == 'July') or (month == 'August') or (month == 'September' and day < 22):
            season = "Summer"
        elif (month == 'September' and day >= 22) or (month == 'October') or (month == 'November') or (month == 'December' and day < 21):
            season = "Fall"
        else:
            print("Invalid date. Please check the month and day entered.")
            return
        
        # Print the result
        print(f"{month} {day} is in {season}.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the day.")

# Call the function
determine_season()

# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Set the fixed number to be guessed
    target_number = 42
    attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")

    for attempt in range(1, attempts + 1):
        # Prompt the user to guess a number
        guess_input = input(f"Attempt {attempt}: Enter your guess: ")

        try:
            # Convert the input to an integer
            guess = int(guess_input)

            # Check if the guess is correct
            if guess == target_number:
                print("Congratulations, you guessed correctly!")
                return
            else:
                # Provide hints
                if guess < target_number:
                    print("Guess is too low.")
                elif guess > target_number:
                    print("Guess is too high.")

                # Indicate last chance on the fifth attempt
                if attempt == attempts:
                    print("Last chance!")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("Sorry, you failed to guess the number in five attempts.")

# Call the function
guess_number()