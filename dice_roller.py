import random

def roll_dice(number_of_dice):
    # Create an empty list to store the results of each die
    rolls = []
    
    # Loop through the number of dice the user wants
    for _ in range(number_of_dice):
        # Randomly pick a number between 1 and 6
        result = random.randint(1, 6)
        rolls.append(result) # Add it to our list
        
    return rolls

# --- Main Program ---
if __name__ == "__main__":
    print("--- Python Dice Roller ---")
    
    try:
        # Ask the user for the number of dice
        num_dice = int(input("How many dice do you want to roll? (e.g., 2): "))
        
        if num_dice <= 0:
            print("Please enter a number greater than 0.")
        else:
            # Roll the dice
            dice_results = roll_dice(num_dice)
            
            # Calculate the total
            total = sum(dice_results)
            
            # Print the results in a clean format
            print(f"\nYou rolled: {dice_results}")
            print(f"Total: {total}")
            
    except ValueError:
        print("Error: Please enter a valid whole number.")
