import secrets, mnemonic
from tkinter import *

window = Tk()
window.title("Seed Generator")
window.columnconfigure([0, 1, 2, 3, 4], minsize=180)

def generate12():
    language = 'english'
    seed = secrets.token_bytes(16)
    mnemonic_words = mnemonic.Mnemonic(language).to_mnemonic(seed)
    mnemonic_word_list = " ".join(mnemonic_words.split())
    print(mnemonic_word_list)
    string_var.set(mnemonic_word_list)

def generate15():
    language = 'english'
    seed = secrets.token_bytes(20)
    mnemonic_words = mnemonic.Mnemonic(language).to_mnemonic(seed)
    mnemonic_word_list = " ".join(mnemonic_words.split())
    print(mnemonic_word_list)
    string_var.set(mnemonic_word_list)

def generate18():
    language = 'english'
    seed = secrets.token_bytes(24)
    mnemonic_words = mnemonic.Mnemonic(language).to_mnemonic(seed)
    mnemonic_word_list = " ".join(mnemonic_words.split())
    print(mnemonic_word_list)
    string_var.set(mnemonic_word_list)

def generate21():
    language = 'english'
    seed = secrets.token_bytes(28)
    mnemonic_words = mnemonic.Mnemonic(language).to_mnemonic(seed)
    mnemonic_word_list = " ".join(mnemonic_words.split())
    print(mnemonic_word_list)
    string_var.set(mnemonic_word_list)

def generate24():
    language = 'english'
    seed = secrets.token_bytes(32)
    mnemonic_words = mnemonic.Mnemonic(language).to_mnemonic(seed)
    mnemonic_word_list = " ".join(mnemonic_words.split())
    print(mnemonic_word_list)
    string_var.set(mnemonic_word_list)

btn_12 = Button(text = "Generate 12-Word Seed", command = generate12)
btn_15 = Button(text = "Generate 15-Word Seed", command = generate15)
btn_18 = Button(text = "Generate 18-Word Seed", command = generate18)
btn_21 = Button(text = "Generate 21-Word Seed", command = generate21)
btn_24 = Button(text = "Generate 24-Word Seed", command = generate24)

string_var = StringVar()
seed = Entry(textvariable = string_var)

btn_12.grid(row=0, column=0, sticky="nsew")
btn_15.grid(row=0, column=1, sticky="nsew")
btn_18.grid(row=0, column=2, sticky="nsew")
btn_21.grid(row=0, column=3, sticky="nsew")
btn_24.grid(row=0, column=4, sticky="nsew")
seed.grid(row=1, columnspan=5, sticky="nsew")

window.mainloop()
