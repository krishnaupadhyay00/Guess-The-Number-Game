import tkinter as tk
from tkinter import messagebox

# Fixed number
SECRET_NUMBER = 56

# Function to check guess
def check_guess():
    try:
        guess = int(entry.get())
        if guess == SECRET_NUMBER:
            messagebox.showinfo("Result 🎉", "Correct!  You guessed the right number.")
        elif guess < SECRET_NUMBER:
            messagebox.showwarning("Hint ", "Too Low! Try a bigger number.")
        else:
            messagebox.showwarning("Hint ", "Too High! Try a smaller number.")
    except ValueError:
        messagebox.showerror("Error ", "Please enter a valid number!")

# Main window
root = tk.Tk()
root.title(" Number Guessing Game ")
root.geometry("400x350")
root.config(bg="#1e1e2e")  # Dark theme background

# Heading
title_label = tk.Label(root, text="🎮 Guess The Number 🎮", 
                       font=("Comic Sans MS", 18, "bold"), 
                       fg="cyan", bg="#1e1e2e")
title_label.pack(pady=20)

# Instruction
inst_label = tk.Label(root, text="Enter a number between 1 and 100", 
                      font=("Arial", 12), fg="white", bg="#1e1e2e")
inst_label.pack(pady=10)

# Entry box
entry = tk.Entry(root, font=("Arial", 14), justify="center", bd=3, relief="solid")
entry.pack(pady=10)

# Button
guess_btn = tk.Button(root, text="Check Guess ", command=check_guess, 
                      font=("Arial", 12, "bold"), bg="lime", fg="black", 
                      relief="raised", bd=4, width=15)
guess_btn.pack(pady=15)

# Footer
footer_label = tk.Label(root, text="Made by Krishna 💻", 
                        font=("Courier New", 10, "italic"), 
                        fg="lightgray", bg="#202e1e")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
