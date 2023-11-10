import random

try:
    num_sides = int(input("Enter the number of sides on the dice: "))
    num_rolls = int(input("Enter how many times you want to roll the dice: "))
    
    if num_sides < 2 or num_rolls < 1:
        raise ValueError("Oops! The dice must have at least 2 sides, and you need to roll it at least once.")

    print(f"Rolling a {num_sides}-sided dice {num_rolls} times:")
    
    for i in range(num_rolls):
        roll_result = random.randint(1, num_sides)
        print(f"Roll {i + 1}: {roll_result}")

except ValueError as ve:
    print(f"Oops! Something went wrong: {ve}")
