import random


def take_pencils(pencils_count, player_name):
    """
    Simulates a player's turn in a pencil-taking game, handling input validation and updating remaining pencils.

    Parameters:
       pencils_count (int): The initial number of pencils available.
       player_name (str): The name of the player taking their turn.

    Returns:
       int: The updated number of pencils remaining after the player's turn.
    """
    while True:
        try:
            pencils_taken = input(f"{player_name}'s turn: ")
            if not pencils_taken.isdigit():
                raise ValueError("Possible values: '1', '2' or '3'")
            elif int(pencils_taken) < 1 or int(pencils_taken) > 3:
                raise ValueError("Possible values: '1', '2' or '3'")
            elif int(pencils_taken) > pencils_count:
                raise ValueError("Too many pencils were taken")
            else:
                pencils_count -= int(pencils_taken)
                print("|" * pencils_count)
                return pencils_count
        except ValueError as ve:
            print(ve)


def bot_turn(pencils_count):
    """
    Performs the bot's turn in a pencil-taking game, strategically choosing how many pencils to remove.

    Parameters:
        pencils_count (int): The number of pencils remaining before the bot's turn.

    Returns:
        int: The updated number of pencils remaining after the bot's turn.
    """
    if pencils_count % 4 == 1:
        pencils_taken = 1
    elif pencils_count % 4 == 0:
        pencils_taken = random.randint(1, 3)
    else:
        pencils_taken = pencils_count % 4
    pencils_count -= pencils_taken
    print(f"Bot's turn: {pencils_taken}")
    print("|" * pencils_count)
    return pencils_count


def main():
    """
    This function simulates a two-player pencil-taking game where players take turns removing pencils from a pile. The
    last player to remove a pencil wins the game.

    Parameters:
        None

    Return:
        None (prints the winner message to the console)
    """
    while True:
        try:
            pencils_count = int(input("How many pencils would you like to use: "))
            if pencils_count <= 0:
                raise ValueError("The number of pencils should be positive")
            break
        except ValueError as ve:
            print(ve)

    while True:
        try:
            choice = input("Choose your player (John or Jack): ")
            if choice not in ["John", "Jack"]:
                raise ValueError("Choose between 'John' and 'Jack'")
            break
        except ValueError as ve:
            print(ve)

    player_name = choice
    bot_name = "Jack" if player_name == "John" else "John"

    while pencils_count > 0:
        if player_name == choice:
            pencils_count = take_pencils(pencils_count, player_name)
            if pencils_count == 0:
                print(f"{player_name} won!")
                break
            pencils_count = bot_turn(pencils_count)
            if pencils_count == 0:
                print(f"{bot_name} won!")
                break
        else:
            pencils_count = bot_turn(pencils_count)
            if pencils_count == 0:
                print(f"{bot_name} won!")
                break
            pencils_count = take_pencils(pencils_count, player_name)
            if pencils_count == 0:
                print(f"{player_name} won!")
                break


if __name__ == "__main__":
    main()
