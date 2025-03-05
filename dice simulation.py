import random

def roll_dice():
    # Simulate rolling two dice by generating random numbers between 1 and 6
    die1 = random.randint(1, 6)
    return die1

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        input("Press Enter to roll the dice...")
        die1 = roll_dice()
        print(f"You rolled a {die1} !")
        print(f"Total: {die1}")
        
        # Ask if the user wants to roll again
        again = input("Do you want to roll again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
