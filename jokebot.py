# Name: Senal Dampiya Dolage
# Student Number: 


# Import the required modules.
import tkinter as tk
import tkinter.messagebox as messagebox
import json


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data file and creating the user interface.
        self.root = tk.Tk()
        self.root.title("Joke Bot")
        self.root.minsize(400, 300)  # Minimum size of the window.

        self.currentJoke = {}  # Initialize self.currentJoke to empty.
        self.currentJokeIndex = 0 # Initialize current joke index to 0 to increment later.

        try:
            file = open('data.txt', 'r')
            self.data = json.load(file)
            file.close()
        except FileNotFoundError:
            messagebox.showerror("Error", "Missing file: data.txt does not exist.")
            self.root.destroy()
            return
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid file: data.txt does not contain valid JSON data.")
            self.root.destroy()
            return

        # Create a Frame to hold the widgets
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20, padx=10)

        # Label to show the joke setup
        self.joke_setup_label = tk.Label(self.frame, text="", font=("Arial", 22), pady=10)
        self.joke_setup_label.pack()

        # Label to show the joke punchline
        self.joke_punchline_label = tk.Label(self.frame, text="", font=("Arial", 16, "italic"))
        self.joke_punchline_label.pack()

        # Label to show the joke ratings
        self.rating_label = tk.Label(self.frame, text="", font=("Arial", 11), pady=15)
        self.rating_label.pack()

        # Second frame to align bottom widgets.
        second_frame = tk.Frame(self.frame)
        second_frame.pack(side="bottom")

        # Label to your rating text
        tk.Label(second_frame, text="Your Rating:").pack(side="left")

        # Entry widget for user rating input
        self.rating_entry = tk.Entry(second_frame, width=5)
        self.rating_entry.pack(padx=5, side="left")

        # Button for submitting the rating
        tk.Button(second_frame, text="Submit", command=self.rateJoke).pack(side="left")

        self.showJoke()
        self.root.mainloop()


    def showJoke(self):
        # This method is responsible for displaying a joke in the GUI.
        self.currentJoke = self.data[self.currentJokeIndex]
        self.joke_setup_label.config(text=self.currentJoke["setup"])
        self.joke_punchline_label.config(text=self.currentJoke["punchline"])

        # Check if the joke has been rated
        if self.currentJoke["numOfRatings"] == 0:
            self.rating_label.config(text="Joke has not been rated")
        else:
            average_rating = round(self.currentJoke["sumOfRatings"] / self.currentJoke["numOfRatings"], 1)
            self.rating_label.config(text=f"Rated {self.currentJoke['numOfRatings']} time(s). Average rating is {average_rating}/5.")

        # Set focus to the rating Entry widget
        self.rating_entry.focus_set()


    def rateJoke(self):
        # This method is responsible for validating and recording the rating that a user gives a joke.
        # Perform rating processing logic here
        rating = self.rating_entry.get()
        if not rating.isdigit() or not 1 <= int(rating) <= 5:
            messagebox.showerror("Rating Error", "Invalid rating! Enter an integer between 1 and 5.")
            return

        rating = int(rating)

        joke = self.currentJoke
        joke["numOfRatings"] += 1
        joke["sumOfRatings"] += rating

        file = open('data.txt', 'w')
        json.dump(self.data, file)
        file.close()

        if self.currentJokeIndex == len(self.data) - 1:
            # No more items in self.data
            messagebox.showinfo("Rating Recorded", "That was the last joke. The program will end now.")
            self.root.destroy()
        else:
            messagebox.showinfo("Rating Recorded", "Thank you for rating! The next joke will appear.")
            # Go to next joke.
            self.currentJokeIndex = self.currentJokeIndex + 1
            self.rating_entry.delete(0, tk.END)
            self.showJoke()


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
