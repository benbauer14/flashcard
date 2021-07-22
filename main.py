BACKGROUND_COLOR = "#B1DDC6"
import tkinter
import random
import csv

# ------------UI---------------
window = tkinter.Tk()
window.title("Flash Cards")
window.minsize(width=800, height=650)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas_card = tkinter.Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0 )
flash_card_front = tkinter.PhotoImage(file="images/card_front.png")
canvas_card.create_image(410, 300, image=flash_card_front)
canvas_card.grid(column=1, row=1,columnspan=2, rowspan=10)

canvas_right = tkinter.Canvas(width=150, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
correct = tkinter.PhotoImage(file="images/right.png")
canvas_right.create_image(90,60,image=correct)
canvas_right.grid(column=1, row=11)

canvas_wrong = tkinter.Canvas(width=200, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong = tkinter.PhotoImage(file="images/wrong.png")
canvas_wrong.create_image(90,60,image=wrong)
canvas_wrong.grid(column=2, row=11)


window = tkinter.mainloop()