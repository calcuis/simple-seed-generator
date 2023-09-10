## simple-seed-generator

**Generate a 12/15/18/21/24-word seed**

This Python code is a simple graphical user interface (GUI) application that generates cryptographic seed phrases of varying word lengths (12, 15, 18, 21, and 24 words) using the secrets and mnemonic libraries. Here's a breakdown of what the code does:

Import necessary libraries:

`secrets`: This library is used for generating secure random numbers, which are used to create cryptographic seed values.

`mnemonic`: This library is used to convert the randomly generated seed values into human-readable mnemonic phrases (this is an external library, might need to execute `pip install mnemonic` for pre-installation; if you do not want to use this library, please refer to the seed-generator-py repo, it will help you to build one all depends on internal libraries).

Tk from `tkinter`: This library provides tools for creating GUI applications.

Create a GUI window:
- The code initializes a Tkinter window with the title "Seed Generator" and configures the column widths for the layout.

The first part (of the code) defines a function for generating seed phrases of different lengths (in terms of word count). Each function does the following:
- Sets the language variable to 'english'.
- Generates a random binary seed value of the specified length using `secrets.token_bytes()`.
- Converts the binary seed into a mnemonic phrase using the `mnemonic.Mnemonic(language).to_mnemonic(seed)` method.
- Prints the mnemonic phrase to the console.

The second part (of the code) creates five buttons labeled with their respective seed phrase lengths:
- Each button is associated with its corresponding generate function through the command attribute.

Create an Entry field for displaying the generated seed phrase (coz allowing copy/cut & paste afterwards which Label field does not):
- The code creates a single-line text entry widget (seed) to display the generated mnemonic phrase.

Layout the GUI elements:
- The buttons and the entry field are placed in the window using the grid layout manager.
- Start the GUI event loop.

The code enters the Tkinter main event loop using `window.mainloop()`, which keeps the GUI application running and responsive to user interactions.
When you run this code, you will have a GUI application with buttons to generate different-length seed phrases, and the generated phrase will be displayed in the text entry field when you click a button.
