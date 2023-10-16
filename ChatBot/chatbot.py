def main():
    """ ChatBot project """
    # Task 1
    print("Hello! My name is Mr.Bot.")
    print("I was created in 2023.")
    # Task 2
    your_name = input("Please, remind me your name: ")
    print("What a great name you have, " + str(your_name))
    # Task 3
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder_3 = input("Remainder of 3: ")
    remainder_5 = input("Remainder of 5: ")
    remainder_7 = input("Remainder of 7: ")
    age = (int(remainder_3) * 70 + int(remainder_5) * 21 + int(remainder_7) * 15) % 105
    print("Your age is " + str(age) + "; that's a good time to start programming!")
    # Task 4
    print("Now I will prove to you that I can count to any number you want.")
    ar_one = int(input("Enter a positive number: "))
    i = 0
    while i <= ar_one:
        print(i, "!")
        i += 1
    print("Completed, have a nice day!")
    # Task 5
    question = "What data type is used to store real numbers in Python?"
    answers = ["int", "float", "complex", "bool"]
    correct_answer = "float"

    while True:
        print(question)
        for index, answer in enumerate(answers):
            print(f"{index + 1}. {answer}")

        user_answer = input("Enter the answer: ")
        user_answer = int(user_answer) - 1

        if user_answer == answers.index(correct_answer):
            print("True! The test is complete.")
            break
        else:
            print("Incorrect answer. Try again.")
    print("Congratulations, have a nice day!")


main()