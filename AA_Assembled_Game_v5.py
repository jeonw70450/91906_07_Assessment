from tkinter import *
from functools import partial
import csv
import random


class Start:
    def __init__(self):
        background = "#FFF4C3"

        # Start GUI
        self.start_frame = Frame(padx=10, pady=10, bg=background)
        self.start_frame.grid()

        # Country Capital Quiz Heading row 0
        self.capital_label = Label(self.start_frame, text="Country Capital Quiz",
                                   font="Helvetica 30 bold", bg=background)
        self.capital_label.grid(row=0)

        # Sub text and Instructions for the game row 1
        self.subtext_label = Label(self.start_frame, text="How well do you know world's capitals? \n\n"
                                                          "You'll be presented with 15 capitals from a list of 242 "
                                                          "capitals.\n "
                                                          "You'll need to match the capitals with their corresponding "
                                                          "country. \n\n "
                                                          "Please select the difficulty you wish to play.",
                                   font="Arial 10", bg=background)
        self.subtext_label.grid(row=1)

        # to_game button frame row 2
        self.to_game_frame = Frame(self.start_frame, bg=background)
        self.to_game_frame.grid(row=2)

        # Button Font
        button_font = "Arial 15 bold"

        # to_game buttons row 2.0
        self.easy_button = Button(self.to_game_frame, text="Easy", font=button_font, bg="#99CCFF",
                                  command=self.to_easy, height=2, width=13, borderwidth=2)
        self.easy_button.grid(row=0, column=0, padx=10, pady=5)

        self.hard_button = Button(self.to_game_frame, text="Hard", font=button_font, bg="#FFBAB8",
                                  command=self.to_hard, height=2, width=13, borderwidth=2)
        self.hard_button.grid(row=0, column=1, padx=10, pady=5)

        # Help Button row 3
        self.help_button = Button(self.start_frame, text="Help", font="Helvetica 10 bold", height=2, width=10,
                                  borderwidth=3, command=self.help)
        self.help_button.grid(row=3, pady=5)

    def to_easy(self):
        Easy()
        self.start_frame.destroy()

    def to_hard(self):
        Hard()
        self.start_frame.destroy()

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="The quiz will present you with a capital \n\n You must identify the "
                                          "corresponding country.\n\n There "
                                          "are a total of 15 rounds.\n\n"
                                          "Easy mode is a multiple choice quiz.\n"
                                          "Hard mode you must type in the answer.")


class Help:
    def __init__(self, partner):
        background = "#FFF4C3"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press 'x' cross at the top, closes help and 'releases' help button.
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Information",
                                 font=("Helvetica", "24", "bold",),
                                 bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", font="helvetica",
                               width=40, bg=background, wrap=500)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="maroon", fg="white",
                                  font="Helvetica" "10" "bold", command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


def to_quit():
    root.destroy()


class Easy:
    def __init__(self):

        # Background color is light yellow
        background = "#FFF4C3"

        # Import the csv file, name of csv file goes here...
        with open('country-capitals.csv', 'r') as f:
            # make csv file into list
            file = csv.reader(f)
            next(f)
            my_list = list(file)

        # Initial Score
        self.score = 0

        # Amounts of games played
        self.played = 0

        # chooses four different countries / capitals from the list
        question_ans = random.choice(my_list)
        yes = random.choice(my_list)
        no = random.choice(my_list)
        ok = random.choice(my_list)

        # Defining variables for the capitals and countries,
        # question is the capital in question
        # self.answer is the correct answer
        # incorrect[1,2,3] are the incorrect countries.
        self.question = question_ans[1]
        self.answer = question_ans[0]
        self.hint = question_ans[2]
        incorrect1 = yes[0]
        incorrect2 = no[0]
        incorrect3 = ok[0]

        # I made the button_list a list so the list can be randomized so that the answer button locations is always
        # different.
        button_list = [self.answer, incorrect1, incorrect2, incorrect3]
        random.shuffle(button_list)
        # Defining the randomized list to their corresponding buttons
        self.top_left = button_list[0]
        self.top_right = button_list[1]
        self.bottom_left = button_list[2]
        self.bottom_right = button_list[3]

        # GUI Setup
        self.game_box = Toplevel(bg=background)
        self.game_frame = Frame(self.game_box, bg=background)
        self.game_frame.grid()
        self.game_box.protocol('WM_DELETE_WINDOW', to_quit)

        # Capital Label row 0
        self.capital_label = Label(self.game_frame, text=self.question,
                                   font="Helvetica 15 bold", bg=background)
        self.capital_label.grid(row=0)

        # Label showing correct or incorrect row 1
        self.answer_box = Label(self.game_frame, text="", font="Helvetica 12 italic", width=45, wrap=300, bg=background)
        self.answer_box.grid(row=1)

        # Setup grid for answer buttons row 2
        self.top_answers_frame = Frame(self.game_box, width=50, height=50, bg=background)
        self.top_answers_frame.grid(row=2, padx=5)

        # width, wrap, font height for buttons
        wt = 15
        ht = 2
        wr = 170
        ft = "Helvetica 15"

        # Top level answers buttons row 2.0
        self.top_left_answer_button = Button(self.top_answers_frame, text=self.top_left,
                                             font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                             command=lambda: self.reveal_answer(self.top_left))
        self.top_left_answer_button.grid(column=0, row=0, padx=5, pady=5)

        self.top_right_answer_button = Button(self.top_answers_frame, text=self.top_right,
                                              font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                              command=lambda: self.reveal_answer(self.top_right))
        self.top_right_answer_button.grid(column=1, row=0, padx=5, pady=5)

        # Bottom level answers buttons row 2.1
        self.bottom_left_answer_button = Button(self.top_answers_frame, text=self.bottom_left,
                                                font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                                command=lambda: self.reveal_answer(self.bottom_left))
        self.bottom_left_answer_button.grid(column=0, row=1, padx=5, pady=5)

        self.bottom_right_answer_button = Button(self.top_answers_frame, text=self.bottom_right,
                                                 font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                                 command=lambda: self.reveal_answer(self.bottom_right))
        self.bottom_right_answer_button.grid(column=1, row=1, padx=5, pady=5)

        # Label for the score and games played row 3
        self.score_label = Label(self.game_box, text="{} correct, {} rounds played".format(self.score, self.played),
                                 bg=background)
        self.score_label.grid(row=3)

        # Button frames for next and hint button row 4
        self.button_frame = Frame(self.game_box, bg=background)
        self.button_frame.grid(row=4)

        # The hint button to get the hint for this country row 0 column 0
        self.hint_button = Button(self.button_frame, text="Hint", command=self.to_hint, width=5,
                                  font="Helvetica 10 bold")
        self.hint_button.grid(row=0, column=0, padx=5)

        # The Next button to proceed to the next round row 0 column 1
        self.next_button = Button(self.button_frame, text="Next", command=lambda: self.to_next(my_list), width=5,
                                  font="Helvetica 10 bold")
        self.next_button.grid(row=0, column=1, padx=5)

        # Disable the next button initially,
        self.next_button.config(state=DISABLED)

    def reveal_answer(self, location):

        # Disable all the buttons
        self.top_left_answer_button.config(state=DISABLED)
        self.top_right_answer_button.config(state=DISABLED)
        self.bottom_left_answer_button.config(state=DISABLED)
        self.bottom_right_answer_button.config(state=DISABLED)

        # Enable the next_button
        self.next_button.config(state=NORMAL)

        # Increase total rounds played by 1
        self.played += 1

        # Check if button is correct.
        if location == self.answer:
            self.answer_box.config(text="Correct!", fg="green")
            self.score += 1

        else:
            self.answer_box.config(text="Incorrect, correct country is {}".format(self.answer), fg="red")

        # Update the score that the user has
        self.score_label.config(text="{} correct / {} rounds played".format(self.score, self.played))

    def to_next(self, capital_list):
        # if the amount of rounds played is 15 the player is taken to the end screen
        if self.played == 15:
            End(self.score)
            self.game_box.destroy()

        # Else the quiz repeats and new questions are asked.
        else:
            self.top_left_answer_button.config(state=NORMAL)
            self.top_right_answer_button.config(state=NORMAL)
            self.bottom_left_answer_button.config(state=NORMAL)
            self.bottom_right_answer_button.config(state=NORMAL)
            self.next_button.config(state=DISABLED)
            self.answer_box.config(text="")

            # chooses four different countries / capitals from the list
            question_ans = random.choice(capital_list)
            yes = random.choice(capital_list)
            no = random.choice(capital_list)
            ok = random.choice(capital_list)

            # Defining variables for the capitals and countries,
            # question is the capital in question
            # self.answer is the correct answer
            # incorrect[1,2,3] are the incorrect countries.
            self.question = question_ans[1]
            self.answer = question_ans[0]
            self.hint = question_ans[2]
            incorrect1 = yes[0]
            incorrect2 = no[0]
            incorrect3 = ok[0]

            self.capital_label.config(text=self.question)

            # I made the button_list a list so the list can be randomized so that the answer button locations is always
            # different.
            button_list = [self.answer, incorrect1, incorrect2, incorrect3]
            random.shuffle(button_list)
            self.top_left = button_list[0]
            self.top_right = button_list[1]
            self.bottom_left = button_list[2]
            self.bottom_right = button_list[3]

            # Defining the randomized list to their corresponding buttons
            self.top_left_answer_button.config(text=self.top_left, command=lambda: self.reveal_answer(self.top_left))
            self.top_right_answer_button.config(text=self.top_right, command=lambda: self.reveal_answer(self.top_right))
            self.bottom_left_answer_button.config(text=self.bottom_left,
                                                  command=lambda: self.reveal_answer(self.bottom_left))
            self.bottom_right_answer_button.config(text=self.bottom_right,
                                                   command=lambda: self.reveal_answer(self.bottom_right))

    def to_hint(self):
        get_hint = Hint(self)
        get_hint.help_text.configure(text="The country is located in: {}".format(self.hint))


class Hard:
    def __init__(self):

        # Background color is light yellow
        background = "#FFF4C3"

        # Import the csv file, name of csv file goes here...
        with open('country-capitals.csv', 'r') as f:
            # make csv file into list
            file = csv.reader(f)
            next(f)
            my_list = list(file)

        # choose an item from the main list, this item is itself a list
        question_ans = random.choice(my_list)

        # Initial Score
        self.score = 0

        # Amounts of games played
        self.played = 0

        # first item in small list
        question = question_ans[1]
        self.answer = question_ans[0]
        self.hint = question_ans[2]

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box, bg=background)
        self.game_frame.grid()
        self.game_box.protocol('WM_DELETE_WINDOW', to_quit)

        # Capital Label row 0
        self.capital_label = Label(self.game_frame, text=question,
                                   font="Helvetica 15 bold", bg=background)
        self.capital_label.grid(row=0, padx=5, pady=10)

        # Setup Answer Entry row 1
        self.answer_entry = Entry(self.game_frame, font="Helvetica 15 bold")
        self.answer_entry.grid(row=1, pady=10, padx=30)
        self.answer_entry.focus()
        self.answer_entry.bind('<Return>', lambda e: self.check_answer())

        # Button frame for "guess" and "next" row 2
        self.button_frame = Frame(self.game_frame, bg=background)
        self.button_frame.grid(row=2)

        # Button to press when users have entered the country row 2.0 column 0
        self.answer_button = Button(self.button_frame, text="Guess", font="Helvetica 10 bold",
                                    command=lambda: self.check_answer())
        self.answer_button.grid(row=0, column=0, padx=5)

        # The hint button to get the hint for this country row 2 column 1
        self.hint_button = Button(self.button_frame, text="Hint", command=self.to_hint, width=5,
                                  font="Helvetica 10 bold")
        self.hint_button.grid(row=0, column=1, padx=5)

        # Button to go to the next question row 2.0 column 2
        self.next_button = Button(self.button_frame, text="Next", font="Helvetica 10 bold",
                                  command=lambda: self.next_question(my_list))
        self.next_button.grid(row=0, column=2, padx=5)
        self.next_button.config(state=DISABLED)
        self.next_button.bind('<Return>', lambda e: self.next_question(my_list))

        # Correct or incorrect Label row 3
        self.answer_box = Label(self.game_frame, text="", font="Helvetica", bg=background, width=33)
        self.answer_box.grid(row=3)

        # Total amount of correct answers and games played row 4
        self.points = Label(self.game_frame, text="{} correct / {} rounds played".format(self.score, self.played),
                            font="Helvetica 10", bg=background)
        self.points.grid(row=4)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        self.played += 1
        if user_answer.casefold() == self.answer.casefold():
            self.answer_box.config(text="Correct!", fg="green")
            self.score += 1
            self.answer_entry.config(bg="#ACF392")
        else:
            self.answer_box.config(text="The country is located in {}".format(self.answer), fg="#F62121")
            self.answer_entry.config(bg="#F39292")
        self.next_button.config(state=NORMAL)
        self.answer_button.config(state=DISABLED)
        self.next_button.focus()
        self.points.config(text="{} correct / {} rounds played".format(self.score, self.played))

    def next_question(self, capital_list):
        # When the user has played 15 rounds we take them to the end gui.
        if self.played == 15:
            End(self.score)
            self.game_box.destroy()
        # If they amount of played is not 15 new questions are generated.
        else:
            question_ans = random.choice(capital_list)
            question = question_ans[1]
            self.answer = question_ans[0]
            self.hint = question_ans[2]
            self.capital_label.config(text=question)
            self.answer_entry.delete(0, "end")
            self.answer_box.config(text="")
            self.next_button.config(state=DISABLED)
            self.answer_button.config(state=NORMAL)
            self.answer_entry.config(bg="white")
            self.answer_entry.focus()

    def to_hint(self):
        get_hint = Hint(self)
        get_hint.help_text.configure(text="The country is located in: {}".format(self.hint))


class Hint:
    def __init__(self, partner):
        background = "#FFF4C3"

        # disable hint button
        partner.hint_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press 'x' cross at the top, closes hint and 'releases' hint button.
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Information",
                                 font=("Helvetica", "24", "bold",),
                                 bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", font="helvetica",
                               width=40, bg=background, wrap=200)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="maroon", fg="white",
                                  font="Helvetica" "10" "bold", command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.hint_button.config(state=NORMAL)
        self.help_box.destroy()


class End:
    def __init__(self, score):
        # Background color is light yellow
        background = "#FFF4C3"

        # Accuracy percentage
        percentage = score / 15

        # End Frame
        self.end_box = Toplevel()
        self.end_frame = Frame(self.end_box, bg=background)
        self.end_frame.grid(row=0)
        self.end_box.protocol('WM_DELETE_WINDOW', to_quit)

        # Heading row 0
        self.end_heading = Label(self.end_frame, text="Thanks for playing!", font="Helvetica 25 bold", bg=background)
        self.end_heading.grid(row=0, padx=10)

        # Game statistics row 1
        self.end_stats = Label(self.end_frame, text="You managed to get \n {} \n right out of \n 15 \n\n"
                                                    "Accuracy percentage : {:.2f}%".format(score, percentage),
                               bg=background, font="Helvetica 10")
        self.end_stats.grid(row=1)

        # Button grid row 2
        # Three Different buttons.
        # Export, Retry, Quit
        self.end_buttons = Frame(self.end_frame, bg=background)
        self.end_buttons.grid(row=2)

        # Export button row 0 column 0
        self.end_export_button = Button(self.end_buttons, text="Export", font="Helvetica 10 bold",
                                        command=lambda: self.to_export(), width=8, bg="#99CCFF", height=2)
        self.end_export_button.grid(row=0, column=0, padx=6, pady=5)

        # Retry Button row 0 column 1
        self.end_retry_button = Button(self.end_buttons, text="Retry", font="Helvetica 10 bold",
                                       command=self.to_start, width=8, bg="#FFFF99", height=2)
        self.end_retry_button.grid(row=0, column=1, padx=6, pady=5)

        # Quit button row 0 column 2
        self.end_quit_button = Button(self.end_buttons, text="Quit", font="Helvetica 10 bold",
                                      command=root.quit, width=8, bg="#FFBAB8", height=2)
        self.end_quit_button.grid(row=0, column=2, padx=6, pady=5)

    def to_start(self):
        Start()
        self.end_box.destroy()

    def to_export(self):
        Export(self)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    something = Start()
    root.mainloop()
