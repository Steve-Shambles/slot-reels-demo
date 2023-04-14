""" slot Machine reels demo, A work in progress.
     Note: the fruit gfx are borrowed and are only used
     here for experiments these wont be used in final code"""
import tkinter as tk
from PIL import Image, ImageTk
import random

symbols = {"bar": "bar.png", "cherry": "cherry.png",
           "coin": "coin.png", "lemon": "lemon.png",
           "plum": "plum.png", "tomatoe": "tom.png",}

root = tk.Tk()
root.title("Slot machine reels demo")
canvas_width = 340
canvas_height = 60
symbol_size = 60
num_symbols = 5

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create the symbol labels
symbols_list = list(symbols.keys())
reel = []


def get_five_rnd_symbols():
    """ Randomly choose 5 symbols to place on reels for start up.
        this will eventually be edited so spin_reels can call here to get
        new symbols"""
    for j in range(num_symbols):
        symbol = random.choice(symbols_list)
        symbol_image = Image.open(symbols[symbol])
        symbol_image = symbol_image.resize((symbol_size, symbol_size))
        symbol_photo = ImageTk.PhotoImage(symbol_image)
        symbol_label = canvas.create_image(j * (symbol_size + 10), 0,
                                           anchor=tk.NW, image=symbol_photo)
        reel.append((symbol_label, symbol_photo))
    canvas.update()


def spin_reels():
    spin_btn.config(state="disabled")  # to stop multiclicking
    for j in range(num_symbols):
        # Get a random symbol
        symbol = random.choice(symbols_list)
        symbol_image = Image.open(symbols[symbol])
        symbol_image = symbol_image.resize((symbol_size, symbol_size))
        symbol_photo = ImageTk.PhotoImage(symbol_image)

        old_symbol_label, _ = reel[j]
        new_symbol_label = canvas.create_image(j * (symbol_size + 10),
                                               -symbol_size, anchor=tk.NW,
                                               image=symbol_photo)
        for k in range(symbol_size // 2):
            canvas.move(old_symbol_label, 0, 2)
            canvas.move(new_symbol_label, 0, 2)
            canvas.update()
            canvas.after(10)

        canvas.delete(old_symbol_label)
        reel[j] = (new_symbol_label, symbol_photo)

        # Print out final reel combination, eventually for checking for win
        symbol_image = symbols[symbol][:-4]  # remove ".png"
        print(symbol_image)

    print('-------')
    spin_btn.config(state="normal")

spin_btn = tk.Button(root, text="Spin", command=spin_reels)
spin_btn.grid(row=1, column=1)


get_five_rnd_symbols()

root.mainloop()
