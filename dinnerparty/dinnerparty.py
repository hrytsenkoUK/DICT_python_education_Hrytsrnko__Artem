import random


def dinner_party():
    try:
        number_of_guests = int(input("Enter the number of guests joining (including you): "))

        if number_of_guests < 1:
            raise ValueError("Please enter a valid number of guests (1 or more).")

        guests = {}

        for i in range(1, number_of_guests + 1):
            name = input("What is the name of guest number {}? ".format(i))
            guests[name] = 0

        total_amount = float(input("Enter the total amount: "))
        per_guest_amount = round((total_amount / number_of_guests), 2)

        for name, amount in guests.items():
            guests[name] = per_guest_amount

        lucky = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: ")

        if lucky == "Yes":
            lucky_guest = random.choice(list(guests.keys()))
            for name in guests.keys():
                if name != lucky_guest:
                    guests[name] = round((total_amount / (number_of_guests - 1)), 2)

            guests[lucky_guest] = 0
            print(f"{lucky_guest} is the lucky one!")
            print(guests)

        else:
            print(guests)
    except ValueError as e:
        print("Error:", e)
        dinner_party()


dinner_party()
