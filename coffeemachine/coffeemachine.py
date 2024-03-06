class CoffeeMachine:
    def __init__(self):
        """
        Initializes the coffee machine with starting resource levels and monetary state.

        This special method, known as the constructor, is automatically called when a new instance of the
        `CoffeeMachine` class is created. It sets the initial values for the following essential attributes:

        * `water`: The amount of water available in the machine (initially 400 units).
        * `milk`: The amount of milk available in the machine (initially 540 units).
        * `coffee_beans`: The amount of coffee beans available in the machine (initially 120 units).
        * `disposable_cups`: The number of disposable cups available in the machine (initially 9).
        * `money`: The amount of money collected by the machine (initially 550 units).

        Arguments:
            None

        Returns:
            None (constructor methods do not return a value)
        """
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def remaining(self):
        """
        Displays the current resource levels and monetary state of the coffee machine.

        This function provides a detailed overview of the internal state of the machine, helping users understand its
        available resources and financial status. It prints information about:

        * `water`: The amount of water available in the machine (units).
        * `milk`: The amount of milk available in the machine (units).
        * `coffee_beans`: The amount of coffee beans available in the machine (units).
        * `disposable_cups`: The number of disposable cups available in the machine.
        * `money`: The amount of money collected by the machine (currency units).

        Arguments:
            self (CoffeeMachine): The instance of the `CoffeeMachine` class for which to display information.

        Returns:
            None (the function prints information to the console but doesn't return a value).
        """
        print(f"The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"{self.money} of money")

    def buy(self):
        """
        Processes customer coffee purchases and updates the machine's inventory.

        This function handles customer coffee purchases by:

        1. Displaying a coffee menu with available options.
        2. Taking the customer's choice as input.
        3. Checking if the requested coffee can be made with available resources.
        4. If sufficient resources are available:
            * Printing a confirmation message.
            * Updating the machine's water, milk, coffee beans, disposable cups, and money based on the chosen coffee.
        5. If resources are insufficient, printing an appropriate error message.

        Arguments:
            self (CoffeeMachine): An instance of the `CoffeeMachine` class.

        Returns:
            None (the function performs actions but doesn't explicitly return a value).
        """
        coffee_menu = {
            1: {"name": "espresso", "water": 250, "milk": 0, "coffee_beans": 16, "cost": 4},
            2: {"name": "latte", "water": 350, "milk": 75, "coffee_beans": 20, "cost": 7},
            3: {"name": "cappuccino", "water": 200, "milk": 100, "coffee_beans": 12, "cost": 6}
        }

        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = input()
        if choice == 'back':
            return
        choice = int(choice)
        coffee = coffee_menu.get(choice)
        if coffee:
            if self.water < coffee["water"]:
                print("Sorry, not enough water!")
            elif self.milk < coffee["milk"]:
                print("Sorry, not enough milk!")
            elif self.coffee_beans < coffee["coffee_beans"]:
                print("Sorry, not enough coffee beans!")
            elif self.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= coffee["water"]
                self.milk -= coffee["milk"]
                self.coffee_beans -= coffee["coffee_beans"]
                self.disposable_cups -= 1
                self.money += coffee["cost"]
        else:
            print("Invalid choice!")

    def fill(self):
        """
        Refills the coffee machine's resources as instructed by the user.

        This function allows the user to manually replenish the machine's water, milk, coffee beans, and disposable
        cups. It prompts the user for the quantity of each resource to add and updates the corresponding attributes
        accordingly.

        Arguments:
            self (CoffeeMachine): An instance of the `CoffeeMachine` class.

        Returns:
            None (the function performs actions but doesn't explicitly return a value).
        """
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.disposable_cups += int(input())

    def take(self):
        """
        Retrieves and removes all accumulated money from the coffee machine.

        This function dispenses the current amount of money collected by the machine and resets the `money` attribute
        to zero. It simulates returning the collected money to the user.

        Arguments:
            self (CoffeeMachine): An instance of the `CoffeeMachine` class.

        Returns:
            None (the function performs actions but doesn't explicitly return a value).
        """
        print(f"I gave you ${self.money}")
        self.money = 0

    def process_action(self, action):
        """
        Performs the requested action based on user input.

        This function acts as a central handler for different coffee machine operations. It takes user-provided action
        commands ("remaining", "buy", "fill", "take") and executes the corresponding methods:

        * `remaining`: Displays current resource levels and money.
        * `buy`: Processes coffee purchases and updates resources.
        * `fill`: Refills machine resources based on user prompts.
        * `take`: Collects and removes all accumulated money.

        Arguments:
            self (CoffeeMachine): An instance of the `CoffeeMachine` class.
            action (str): The user-specified action command.

        Returns:
            None (the function performs actions but doesn't explicitly return a value).
        """
        if action == "remaining":
            self.remaining()
        elif action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()


def main():
    """
    Entry point for the coffee machine program.

    This function serves as the main loop of the program, interacting with the user and managing the coffee machine operations. It continuously:

    1. Prints a menu of available actions ("buy", "fill", "take", "remaining", "exit").
    2. Prompts the user for their desired action.
    3. If the action is "exit", terminates the loop.
    4. Otherwise, processes the action by calling the `coffee_machine.process_action` method.

    Arguments:
        None (directly executed as the program's entry point).

    Returns:
        None (the function executes the loop and doesn't explicitly return).
    """
    coffee_machine = CoffeeMachine()
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "exit":
            break
        coffee_machine.process_action(action)


if __name__ == "__main__":
    main()
