from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from sympy import sympify, SympifyError
import random


# TODO:
#   - [] add general game information popup box and icon
#   - [] implement effects


# main layout: calculator
#    _______ 
#    c ( ) /
#    7 8 9 *
#    4 5 6 -
#    1 2 3 +
#     _0_  =

# left side: info
#   score: 
#   target: 
#   presses: 
#   effect: 
#   effect info button

# initialize random seed
random.seed()

# values to keep track of
scoreVal = 0
current = random.randint(0, 99) # start with a random 2 digit number
curr_text = f"{current}"
targetVal = 100
numButtonPresses = 20
curr_digit = len(str(current))
curr_effect = 0
effects = [ # list of tuples: name, desc
    ("None", "No effect."),
    ("No evens", "No even-numbered buttons can be used."),
    ("No odds", "No odd-numbered buttons can be used."),
    ("Only squares", "Only square buttons (1, 4, 9) can be used."),
    ("No multiplication", "Cannot use the multiply button.")
]
disabled = [] # strings of labels that are disabled

def next_round():
    global numButtonPresses, curr_text, scoreVal, targetVal, current, curr_digit
    
    # update values
    scoreVal += int(1.0/(abs(current - targetVal) + 1) * 100) + numButtonPresses * 10
    numButtonPresses = 20
    current = random.randint(0, 99)
    curr_digit = len(str(current))
    curr_text = f"{current}"
    targetVal *= 2
    
    # update labels
    text["text"] = curr_text
    score["text"] = f"Score: {scoreVal}"
    target["text"] = f"Target: {targetVal}"
    presses["text"] = f"Presses: {numButtonPresses}"

# handle each button
def button_press(button):
    global numButtonPresses, curr_text, curr_digit, scoreVal, current
    
    # update presses
    numButtonPresses -= 1
    presses["text"] = f"Presses: {numButtonPresses}"
    
    if numButtonPresses == 0:
        next_round()
        return
    
        
    if button == "=": # acts as the submit button
        curr_digit = 0
        try: # update current
            current = sympify(curr_text)
            if current == targetVal:
                next_round()
                return
            curr_text = str(current)
            text["text"] = curr_text
        except SympifyError:
            # popup box, deduct points
            print("subtracting points")
            scoreVal -= 10
            pass
        return
    
    if button == "c":
        curr_digit = 0
        curr_text = ""
        text["text"] = ""
        return
    
    if button in [str(n) for n in range(10)] and button not in disabled:
        if curr_digit < 2:
            curr_digit += 1
            curr_text += button
            text["text"] = curr_text
        else:
            numButtonPresses += 1 # give back button press
            presses["text"] = f"Presses: {numButtonPresses}"
    elif button not in disabled:
        curr_digit = 0
        curr_text += button
        text["text"] = curr_text
    


root = Tk()
root.title("The Calculator Game")

# left side
ltextfont = font.Font(family="Arial", size=20)
lbuttonfont = font.Font(family="Arial", size=10)
gameinfo = """
You can only enter up to a 2-digit number before you must perform an operation.

Try to get as close to the target as possible -- the closer you are, the more points you get.
"""
score = Label(root, text=f"Score: {scoreVal}", padx=10, font=ltextfont)
target = Label(root, text=f"Target: {targetVal}", padx=10, font=ltextfont)
presses = Label(root, text=f"Presses: {numButtonPresses}", padx=10, font=ltextfont)
effect = Label(root, text="Effect: none", padx=10, font=ltextfont)
effect_info = Button(root, text="Effect Info", width=6, height=1, command=lambda: messagebox.showinfo(effects[curr_effect][0], effects[curr_effect][1]), font=lbuttonfont)
game_info = Button(root, text="Game Info", width=6, height=1, command=lambda: messagebox.showinfo("Game Information", gameinfo), font=lbuttonfont)

# main calculator
text = Label(root, text=f"{current}", font=("Arial",25))

clear = Button(root, text="c", width=3, height=2, command=lambda: button_press("c"))
openP = Button(root, text="(", width=3, height=2, command=lambda: button_press("("))
closeP = Button(root, text=")", width=3, height=2, command=lambda: button_press(")"))
divide = Button(root, text="/", width=3, height=2, command=lambda: button_press("/"))

seven = Button(root, text="7", width=3, height=2, command=lambda: button_press("7"))
eight = Button(root, text="8", width=3, height=2, command=lambda: button_press("8"))
nine = Button(root, text="9", width=3, height=2, command=lambda: button_press("9"))
mult = Button(root, text="*", width=3, height=2, command=lambda: button_press("*"))

four = Button(root, text="4", width=3, height=2, command=lambda: button_press("4"))
five = Button(root, text="5", width=3, height=2, command=lambda: button_press("5"))
six = Button(root, text="6", width=3, height=2, command=lambda: button_press("6"))
sub = Button(root, text="-", width=3, height=2, command=lambda: button_press("-"))

one = Button(root, text="1", width=3, height=2, command=lambda: button_press("1"))
two = Button(root, text="2", width=3, height=2, command=lambda: button_press("2"))
three = Button(root, text="3", width=3, height=2, command=lambda: button_press("3"))
add = Button(root, text="+", width=3, height=2, command=lambda: button_press("+"))

zero = Button(root, text="0", width=15, height=2, command=lambda: button_press("0"))
enter = Button(root, text="=", width=3, height=2, command=lambda: button_press("="))

# pack all elements
r=0
c=0

score.grid(row=r, column=c, sticky="w")
target.grid(row=r+1, column=c, sticky="w")
presses.grid(row=r+2, column=c, sticky="w")
effect.grid(row=r+3, column=c, sticky="w")
effect_info.grid(row=r+4, column=c, sticky="n")
game_info.grid(row=r+5, column=c)
c += 1

Label(root, text="         ").grid(row=r, column=c)
c += 1

text.grid(row=r, column=c, columnspan=4)
r += 1

clear.grid(row=r, column=c)
openP.grid(row=r, column=c+1)
closeP.grid(row=r, column=c+2)
divide.grid(row=r, column=c+3)
r += 1

seven.grid(row=r, column=c)
eight.grid(row=r, column=c+1)
nine.grid(row=r, column=c+2)
mult.grid(row=r, column=c+3)
r += 1

four.grid(row=r, column=c)
five.grid(row=r, column=c+1)
six.grid(row=r, column=c+2)
sub.grid(row=r, column=c+3)
r += 1

one.grid(row=r, column=c)
two.grid(row=r, column=c+1)
three.grid(row=r, column=c+2)
add.grid(row=r, column=c+3)
r += 1

zero.grid(row=r, column=c, columnspan=3)
enter.grid(row=r, column=c+3)

root.mainloop()