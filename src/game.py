import tkinter as tk

# main layout: calculator
#    _12|____ 
#    c ( ) /
#    7 8 9 *
#    4 5 6 -
#    1 2 3 +
#     _0_  =

# left side: info
#   score: 
#   target: 123
#   presses: 10 (increases or decreases based on closeness to value)
#   effect: no evens



root = tk.Tk()

# left side
score = tk.Label(root, text="score: 1000000")
target = tk.Label(root, text="target: 123")
presses = tk.Label(root, text="presses: 10")
effect = tk.Label(root, text="effect: no evens   ")


# main calculator
text = tk.Label(root, text="1234567890", font=("Arial",25))

clear = tk.Button(root, text="c", width=3, height=2, command=lambda: score.config(text = "wow!"))
openP = tk.Button(root, text="(", width=3, height=2)
closeP = tk.Button(root, text=")", width=3, height=2)
divide = tk.Button(root, text="/", width=3, height=2)

seven = tk.Button(root, text="7", width=3, height=2)
eight = tk.Button(root, text="8", width=3, height=2)
nine = tk.Button(root, text="9", width=3, height=2)
mult = tk.Button(root, text="*", width=3, height=2)

four = tk.Button(root, text="4", width=3, height=2)
five = tk.Button(root, text="5", width=3, height=2)
six = tk.Button(root, text="6", width=3, height=2)
sub = tk.Button(root, text="-", width=3, height=2)

one = tk.Button(root, text="1", width=3, height=2)
two = tk.Button(root, text="2", width=3, height=2)
three = tk.Button(root, text="3", width=3, height=2)
add = tk.Button(root, text="+", width=3, height=2)

zero = tk.Button(root, text="0", width=15, height=2)
enter = tk.Button(root, text="=", width=3, height=2)

# pack all elements
r=0
c=0

score.grid(row=r, column=c, sticky="w")
target.grid(row=r+1, column=c, sticky="w")
presses.grid(row=r+2, column=c, sticky="w")
effect.grid(row=r+3, column=c, sticky="w")
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