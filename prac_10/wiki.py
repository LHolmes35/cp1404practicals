"""
CP1404 Practical
Learn how to use Wikipedia import
"""

import wikipedia


def main():
    try:
        user_search = input("What would you like to know about? ")
        while user_search != "":
            print(user_search.title, wikipedia.summary(user_search), user_search.url)
            user_search = input("What would you like to know about?")
    except wikipedia.exceptions.DisambiguationError as e:
        wikipedia.page(user_search, auto_suggest=False)


main()
