import secrets, mnemonic
import tkinter as tk

def generate12():
    language = 'english'
    seed = secrets.token_bytes(16)
    mnemonic_words = mnemonic.Mnemonic(language).to_mnemonic(seed)
    mnemonic_word_list = " ".join(mnemonic_words.split())
    print(mnemonic_word_list)
    lbl_result["text"] = mnemonic_word_list
    f=open('seed.txt', 'w')
    f.write(mnemonic_word_list)
    f.close()

def generate24():
    language = 'english'
    seed = secrets.token_bytes(32)
    mnemonic_words = mnemonic.Mnemonic(language).to_mnemonic(seed)
    mnemonic_word_list = " ".join(mnemonic_words.split())
    print(mnemonic_word_list)
    lbl_result["text"] = mnemonic_word_list
    f=open('seed.txt', 'w')
    f.write(mnemonic_word_list)
    f.close()

window = tk.Tk()
window.title("Seed Generator")
window.columnconfigure(0, minsize=800)

btn_12 = tk.Button(text="Generate 12-word Seedphrase", command=generate12)
btn_24 = tk.Button(text="Generate 24-word Seedphrase", command=generate24)
lbl_result = tk.Label(foreground="red")

btn_12.grid(row=0, column=0, sticky="nsew")
btn_24.grid(row=1, column=0, sticky="nsew")
lbl_result.grid(row=2, column=0)

window.mainloop()
