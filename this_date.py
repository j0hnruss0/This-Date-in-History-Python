"""Find a random date in history for trivia facts."""
import sys
import random


def main():
    """Code returns random dates. More features to be added, like a This Date in History Look-up."""
    print("This is the Random Date Generator!\n")
    print("Your lucky date is...\n\n")

    months = ('January', 'February', 'March', 'April', 'May',
              'June', 'July', 'August', 'September', 'October',
              'November', 'December')
    longest_months = ('January', 'March', 'May', 'July', 'August', 'October', 'December')
    no_feb = ('January', 'March', 'April', 'May',
              'June', 'July', 'August', 'September', 'October',
              'November', 'December')

    while True:
        date_day = random.randint(1, 31)
        if date_day == 31:
            date_month = random.choice(longest_months)
        elif date_day == 30:
            date_month = random.choice(no_feb)
        else:
            date_month = random.choice(months)

        print("\n\n")
        print("{} {}".format(date_month, date_day), file=sys.stderr)
        print("\n\n")

        try_again = input("\nTry Again? (Press Enter, or Press 'n' to quit)\n")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit")

if __name__ == "__main__":
    main()
