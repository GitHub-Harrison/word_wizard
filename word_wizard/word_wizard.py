"""
Dictionary/Thesaurus application using an API
"""

import os
import time
import sys
import requests

# consider adding a sub menu to thesaurus to allow for
# selections like synonyms + antonyms etc

def clear():
    """
    Function to clear the terminal to remove clutter
    """
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    """
    Function for a main menu making allowing
    users to decide if they are using the dictionary
    or thesaurus option
    """

    choice = 0
    while choice !=3:
        print("\nWelcome to WordWizard!")
        print("------------------------")
        print("1 - Dictionary")
        print("2 - Thesaurus")
        print("3 - Exit")

        choice = input("Select your choice: ")

        if choice == "1":
            clear()
            print("\nYou have selected the dictionary option.")
            # user_word = input("Enter your word: ")
            dictionary()
        elif choice == "2":
            clear()
            print("\nYou have selected the thesaurus option.")
            thesaurus()
        elif choice == "3":
            print("\nExiting now...")
            sys.exit()
        else:
            print("\nPlease enter a valid selection")
            time.sleep(2)
            clear()

def dictionary():
    """
    Function to get the definitions for the users word
    """
    # datamuse api looks to have an area for definitions md : d
    # look into this more later
    print("\nDictionary feature coming soon!")


def thesaurus():
    """
    Function similar to menu, gives the user different
    options for using the thesaurus (synonyms, antonyms, etc)
    """
    choice = 0
    while choice !=3:
        print("\nThesaurus")
        print("------------------------")
        print("1 - Synonyms")
        print("2 - Antonyms")
        print("3 - Return")

        choice = input("Enter your selection: ")

        if choice == "1":
            clear()
            print("\nYou have selected the synonyms option.")
            user_word = input("Enter your word: ")
            get_synonyms(user_word)
        elif choice == "2":
            clear()
            print("\nYou have selected the antonyms option.")
            user_word = input("Enter your word: ")
            get_antonyms(user_word)
        elif choice == "3":
            clear()
            print("Returning...")
            menu()
        else:
            print("\nPlease enter a valid selection")
            time.sleep(2)
            clear()


def get_synonyms(word):
    """
    Function to get all synonyms listed for the users word
    using Datamuse API
    """

    base_url = "https://api.datamuse.com/words"
    params = {"rel_syn" : word}

    response = requests.get(base_url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()
        synonyms = [entry['word'] for entry in data]
        if synonyms:
            print(f"Synonyms for {word}: {', '.join(synonyms)}")
        else:
            print(f"No synonyms found for {word}.")
    else:
        print(f"API request for synonyms of {word} failed.")


def get_antonyms(word):
    """
    Function to get all antonyms listed for the users word
    using Datamuse API
    """

    base_url = "https://api.datamuse.com/words"
    params = {"rel_ant" : word}

    response = requests.get(base_url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()
        antonyms = [entry['word'] for entry in data]
        if antonyms:
            print(f"Antonyms for {word}: {', '.join(antonyms)}")
        else:
            print(f"No antonyms found for {word}.")
    else:
        print(f"API request for antonyms of {word} failed.")


if __name__ == "__main__":
    menu()
