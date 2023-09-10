import secrets, mnemonic
from tkinter import *

root = Tk()
root.title("Seed Generator")
root.columnconfigure([0, 1, 2, 3, 4], minsize=180)
e = Entry()

def generate(number):
    language = 'english'
    seed = secrets.token_bytes(number)
    mnemonic_words = mnemonic.Mnemonic(language).to_mnemonic(seed)
    mnemonic_word_list = " ".join(mnemonic_words.split())
    print(mnemonic_word_list)
    e.delete(0, END)
    e.insert(0, mnemonic_word_list)

btn_12 = Button(text = "Generate 12-Word Seed", command = lambda: generate(16))
btn_15 = Button(text = "Generate 15-Word Seed", command = lambda: generate(20))
btn_18 = Button(text = "Generate 18-Word Seed", command = lambda: generate(24))
btn_21 = Button(text = "Generate 21-Word Seed", command = lambda: generate(28))
btn_24 = Button(text = "Generate 24-Word Seed", command = lambda: generate(32))
btn_12.grid(row=0, column=0, sticky="nsew")
btn_15.grid(row=0, column=1, sticky="nsew")
btn_18.grid(row=0, column=2, sticky="nsew")
btn_21.grid(row=0, column=3, sticky="nsew")
btn_24.grid(row=0, column=4, sticky="nsew")
e.grid(row=1, columnspan=5, sticky="nsew")

root.mainloop()
