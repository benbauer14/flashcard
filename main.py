BACKGROUND_COLOR = "#B1DDC6"
import tkinter
import random
import csv
import time
from tkinter.constants import COMMAND
master_list = []
words = []
wordsIndex = -1
# ----------LOAD CSV------------
def onLoad():
    with open("data/french_words.csv") as file:
        data_file = csv.reader(file)
        global master_list
        for row in data_file:
            if row[0] == "French":
                pass
            else:
                master_list.append([row[0], row[1]])
# -------Random Word-----------
def randomWord():
    global master_list, words, wordsIndex
    randomitem = random.randint(0, len(master_list) -1)
    wordsIndex = randomitem
    words = master_list[randomitem]
    canvas_card.itemconfig(canvas_text, text=words[0])
    print(f"fr={words[0]} en={words[1]}")
    # return words

# ------------Right Click---------
def correctClick():
    global master_list, fliptimer, words, wordsIndex
    master_list.pop(wordsIndex)
    with open("data/french_words.csv", "w") as file:
        file.write("French,English\n")
        for row in master_list:
            file.write(row[0] + "," + row[1]+"\n")
    window.after_cancel(fliptimer)
    randomWord()
    canvas_card.itemconfig(cards, image=front_card)
    canvas_card.itemconfig(canvas_text, text=words[0],fill="black")
    fliptimer = window.after(3000,func=flipCard)

# ------------Wrong Click---------
def wrongClick():
    global fliptimer, words
    window.after_cancel(fliptimer)
    randomWord()
    canvas_card.itemconfig(cards, image=front_card)
    canvas_card.itemconfig(canvas_text, text=words[0], fill="black")
    fliptimer = window.after(3000,func=flipCard)

# ------------Flip Card-------------
def flipCard():
    global words
    canvas_card.itemconfig(cards, image=back_card)
    canvas_card.itemconfig(canvas_text, text=words[1], fill="white")

# ------------UI--------------

onLoad()
window = tkinter.Tk()
window.title("Flash Cards")
window.minsize(width=800, height=650)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
fliptimer = window.after(3000, func=flipCard)

canvas_card = tkinter.Canvas(width=800, height=550)
front_card = tkinter.PhotoImage(file="images/card_front.png")
back_card = tkinter.PhotoImage(file="images/card_back.png")
cards = canvas_card.create_image(410, 300, image=front_card)
canvas_text = canvas_card.create_text(400, 300, text="", fill="black", font=("Arial", 30, "normal"))
canvas_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card.grid(column=0, row=0,columnspan=2)

wrong = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong, highlightthickness=0, command=wrongClick)
wrong_button.grid(column=0, row=1)

correct = tkinter.PhotoImage(file="images/right.png")
correct_button = tkinter.Button(image=correct, highlightthickness=0, command=correctClick)
correct_button.grid(column=1, row=1)
randomWord()




window = tkinter.mainloop()