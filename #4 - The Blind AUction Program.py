print("Welcome to The Blind Auction! \n")  # Greeting message to introduce the program


# Step to clear the console screen. This will be used to clear the screen after every user input for a clean UI.
def clear_screen():
    print("\n" * 50)


# Todo 1 - Create a List and store keys and values after asking, max upto 3 people.
# We ask the user for their name and bid, and we do this for up to 3 users.
# We'll clear the screen after each user enters their details.
# This keeps the program clean and fresh for every new user.

# Todo 2 - Create an List with the bids of the users in the dictionary 'name'.
# We will use a dictionary to store the 'name' as key and 'bid' as value.
names = []  # List to store user's names (but we'll replace this with a dictionary later)
bids = []  # List to store user bids (this will also be replaced by a dictionary)


# Function to get the user's name and bid.
# It asks the user for their name and bid amount.
# 'input()' is used to get data from the user interactively.
def get_bidder_info():
    name = input("Enter your name please: \n").lower()  # Get the user's name and convert to lowercase for consistency
    bid = int(input(f"Enter {name}'s bid in $: \n"))  # Get the bid value, convert it to an integer
    return name, bid  # Return the name and bid to be used later in the program


# Todo 3 - Store the 'bids' list along with the 'name' list with respect to each user's name along with their bids in a dictionary.
# Instead of using two lists (names and bids), we will now use a dictionary to store user names as keys and their respective bids as values.
bidders = {}  # Create an empty dictionary where key is the 'name' and value is the 'bid'


# Todo 5 - When there are no users left to join in, provide the winner.
# The function 'find_winner()' finds the user with the highest bid.
# It checks for the highest bid in the dictionary and then prints the winner.

def find_winner(bidders):
    highest_bid = max(bidders.values())  # Find the maximum bid value in the dictionary
    # Find the name of the user who made the highest bid by checking for the key with the highest value
    winner_name = [name for name, bid in bidders.items() if bid == highest_bid][0]
    print(f"\nThe winner is {winner_name} with a bid of ${highest_bid}!")  # Display the winner's name and bid


while True:
    # Todo 4 - Ask the user(s) if there are any more users left to join or should we continue?
    # The program asks if another user wants to place a bid.
    # If the answer is "yes", the loop continues. If "no", the program will exit the loop and determine the winner.

    user_name, user_bid = get_bidder_info()  # Get name and bid from the user using the 'get_bidder_info' function
    bidders[user_name] = user_bid  # Store the user's name and bid in the bidders dictionary

    # Ask if there are more users who want to play
    another_user = input("Is there another user who wants to bid? (yes/no): ").lower()  # Input for more users
    clear_screen()  # Clear the screen after each user input for a cleaner interface

    if another_user != "yes":  # If no more users want to bid, exit the loop
        # If no more users, find the winner and exit the loop
        find_winner(bidders)  # Call the function to find the winner from the bidders dictionary
        break  # Exit the loop after the winner has been found and displayed