# Jade's reminder program
# version 1
print("Welcome to your reminder list!")
choice = menu()


def menu():
    option1 = "Print tasks."
    option2 = "Add a task."
    option3 = "Remove a task."

    # TODO: add a number to each option
    # should look like "1. Print Tasks."
    # hint: the term for doing this is concatenation

    # TODO: print each option on its own line

    choice = input("Input option number:")
    return choice;

def useOption(choice):
    # TODO: write if/elif statements for each option
    # if true, print "Option <choice> selected."

    # Consider: what if the user enters something
    # that isn't "1" "2" or "3"?
    # TODO: write code to handle this possibility
    # hint: what is the difference between if, elif, and else?
    return;
