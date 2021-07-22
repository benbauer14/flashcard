BACKGROUND_COLOR = "#B1DDC6"
import tkinter
import random
import csv
import time
master_list = []
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
    global master_list
    randomitem = random.randint(0, len(master_list) -1)
    words = master_list[randomitem]

    return words
# ------------UI---------------
onLoad()
print(randomWord()[1])
window = tkinter.Tk()
window.title("Flash Cards")
window.minsize(width=800, height=650)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas_card = tkinter.Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0 )
flash_card = tkinter.PhotoImage(file="images/card_front.png")
front = canvas_card.create_image(410, 300, image=flash_card)
canvas_text = canvas_card.create_text(400, 300, text="Test", fill="black", font=("Arial", 30, "normal"))
canvas_card.grid(column=1, row=1,columnspan=2, rowspan=10)

canvas_right = tkinter.Canvas(width=150, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
correct = tkinter.PhotoImage(file="images/right.png")
canvas_right.create_image(90,60,image=correct,)
canvas_right.grid(column=1, row=11)

canvas_wrong = tkinter.Canvas(width=200, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong = tkinter.PhotoImage(file="images/wrong.png")
canvas_wrong.create_image(90,60,image=wrong)
canvas_wrong.grid(column=2, row=11)

game_over = False
response = False
while game_over == False:
    word = randomWord()
    canvas_card.delete(canvas_text)
    canvas_text = canvas_card.create_text(400, 300, text=word[0], fill="black", font=("Arial", 30, "normal"))
    canvas_card.update()
    time.sleep(5)
    canvas_card.delete(front)
    flash_card = tkinter.PhotoImage(file="images/card_back.png")
    back = canvas_card.create_image(410, 300, image=flash_card)
    canvas_card.delete(canvas_text)
    canvas_text = canvas_card.create_text(400, 300, text=word[1], fill="black", font=("Arial", 30, "normal"))

    while response == False
# time.sleep(20)
# game_over = True



window = tkinter.mainloop()