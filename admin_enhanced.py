# Name: Senal Dampiya Dolage
# Student Number: 


# Import the json module to allow us to read and write data in JSON format.
import json


# This function repeatedly prompts for input until an integer is entered.
def inputInt(prompt):
    while True:
        value = input(prompt)
        try:
            int_value = int(value)
            if int_value > 0:
                return int_value
            else:
                print("Invalid input. Please enter an integer larger than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


# This function repeatedly prompts for input until something (not whitespace) is entered.
def inputSomething(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value


# This function opens "data.txt" in write mode and writes dataList to it in JSON format.
def saveChanges(dataList):
    file = open('data.txt', 'w')
    json.dump(data, file)
    file.close()


# Function to check if joke is a top joke.
def checkIfTopJoke(joke):
    if joke['numOfRatings'] == 0:
        return False
    average_rating = joke['sumOfRatings'] / joke['numOfRatings']
    return average_rating >= 4


# Open data.txt and read the data / create an empty list if the file does not exist.
try:
    file = open('data.txt', 'r')
    data = json.load(file)
    file.close()
except:
    data = []


# Print welcome message, then enter the endless loop which prompts the user for a choice.
print('Welcome to the Joke Bot Admin Program.')

while True:
    print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete, [t]op or [q]uit.')
    # Prompt for input and convert it to lowercase.
    choice = input('> ').lower()

    if choice == 'a':
        # Add a new joke.
        setup = inputSomething("Enter the setup of the joke: ")
        punchline = inputSomething("Enter the punchline of the joke: ")

        joke = {
            "setup": setup,
            "sumOfRatings": 0,
            "punchline": punchline,
            "numOfRatings": 0
        }

        data.append(joke)
        saveChanges(data)
        print("Joke added and saved!")


    elif choice == 'l':
        # List the current jokes.
        if not data:
            print("No jokes saved.")
        else:
            for i, joke in enumerate(data):
                print(f"{i + 1}) {joke['setup']}")


    elif choice == 's':
        # Search the current jokes.
        search_term = inputSomething("Enter the search term: ").lower()
        search_results = []

        for i, joke in enumerate(data):
            if search_term in joke['setup'].lower() or search_term in joke['punchline'].lower():
                search_results.append((i, joke))

        if not search_results:
            print("No matching jokes found.")
        else:
            for index, result in search_results:
                print(f"[{index + 1}] {result['setup']}")


    elif choice == 'v':
        # View a joke.
        if not data:
            print("No jokes saved.")
        else:
            index = inputInt("Enter the index number of the joke you want to view: ")
            if index < 0 or index-1 > len(data):
                print("Invalid index number.")
            else:
                joke = data[index-1]
                print(f"Setup: {joke['setup']}")
                print(f"Punchline: {joke['punchline']}")
                if joke['numOfRatings'] == 0:
                    print("Joke has not been rated.")
                else:
                    average_rating = joke['sumOfRatings'] / joke['numOfRatings']
                    print(f"Number of ratings: {joke['numOfRatings']}")
                    print(f"Average rating: {average_rating:.1f}")


    elif choice == 'd':
        # Delete a joke.
        if not data:
            print("No jokes saved.")
        else:
            index = inputInt("Enter the index number of the joke you want to delete: ")
            if index < 0 or index-1 >= len(data):
                print("Invalid index number.")
            else:
                del data[index-1]
                saveChanges(data)
                print("Joke deleted.")


    elif choice == 'q':
        # Quit the program.
        print("Goodbye!")
        break


    elif choice == "t":
        # Top jokes
        top_jokes = [joke for joke in data if checkIfTopJoke(joke)]
        if not top_jokes:
            print("No top-rated jokes found.")
        else:
            for i, joke in enumerate(top_jokes):
                print(f"{i + 1}) {joke['setup']}")


    else:
        # Print "invalid choice" message.
        print("Invalid choice. Please try again.")
        pass
