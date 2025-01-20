import tkinter as tk
from tkinter import messagebox
# This function launches a simple gui with a button that will print hello world to the console.
def main():
    def helloWorld():
        print("Hello World!")
    root = tk.Tk()
    root.title("Hello World")
    button = tk.Button(root, text="Hello World", command=helloWorld)
    button.pack()
    root.mainloop()

main()
