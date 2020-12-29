"""Find a random date in history for trivia facts."""
import sys
import random
import requests
from bs4 import BeautifulSoup


def main():
    """Code returns random dates. More features to be added, like a This Date in History Look-up."""
    print("This is the Random Date Generator!\n")

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
        
        response = requests.get(url="https://en.wikipedia.org/wiki/Wikipedia:Selected_anniversaries/" +
                                date_month +
                                "_" +
                                str(date_day))
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find(class_="mw-parser-output").contents[6]
        add_content = soup.find(class_="mw-parser-output").contents[10].find_all("li")

        title_text = ""
        for i in title:
            title_text += i.string

        print("Your lucky date is...{} {}".format(date_month.upper(), str(date_day).upper()), file=sys.stderr)
        print("\n")
        print(title_text)
        print("----Additional events of importance----")
        for j in add_content:
            add_text = ""
            for all in j.contents:
                try:
                    add_text += all.string
                except TypeError:
                    break
            print(add_text)

        try_again = input("\nTry Again? (Press Enter, or Press 'n' to quit)\n")
        if try_again.lower() == "n":
            break

if __name__ == "__main__":
    main()
