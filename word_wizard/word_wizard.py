import requests
import os
import time
import sys

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
    while choice !=4:
        print("\nWelcome to WordWizard!")
        print("------------------------")
        print("1 - Dictionary")
        print("2 - Thesaurus")
        print("3 - Antonyms")
        print("4 - Exit")

        choice = input("Select your choice: ")

        if choice == "1":
            clear()
            print("\nYou have selected the dictionary option.")
            # user_word = input("Enter your word: ")
            dictionary()
        elif choice == "2":
            clear()
            print("\nYou have selected the thesaurus option.")
            user_word = input("Enter your word: ")
            synonyms(user_word)
        elif choice == "3":
            clear()
            print("\nYou have selected the antonyms option.")
            user_word = input("Enter your word: ")
            antonyms(user_word)
        elif choice == "4":
            print("\nExiting now...")
            sys.exit()
        else:
            print("\nPlease enter a valid selection")
            time.sleep(2)
            clear()

def dictionary():
    """
    Function to get the definitions for the users word,
    Datamuse API does not support word definitions so this
    feature will be added another time with a different api.
    """
    print("\nDictionary feature coming soon!")


def synonyms(word):
    """
    Function to get all synonyms listed for the users word
    using Datamuse API
    """

    base_url = "https://api.datamuse.com/words"
    params = {"rel_syn" : word}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        synonyms = [entry['word'] for entry in data]
        if synonyms:
            print(f"Synonyms for {word}: {', '.join(synonyms)}")
        else:
            print(f"No synonyms found for {word}.")
    else:
        print(f"API request for synonyms of {word} failed.")


def antonyms(word):
    """
    Function to get all antonyms listed for the users word
    using Datamuse API
    """

    base_url = "https://api.datamuse.com/words"
    params = {"rel_ant" : word}

    response = requests.get(base_url, params=params)

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