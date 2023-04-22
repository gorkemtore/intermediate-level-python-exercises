from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv(filepath_or_buffer="data/words_to_learn.csv")
except:
    original_data = pandas.read_csv(filepath_or_buffer="data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
print(to_learn)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)

    canvas.itemconfig(card_bg, image=card_front_img)
    canvas.itemconfig(card_title, text=f"French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()

    unknown_words = pandas.DataFrame(to_learn)
    unknown_words.to_csv("data/words_to_learn.csv", index=False)



def flip_card():
    canvas.itemconfig(card_bg, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ------------------------ USER INTERFACE ------------------------------
window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
window.title("Flash Card App")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
