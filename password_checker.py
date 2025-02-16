import re
import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_password_strength(password):
    strength_score = 0

    if len(password) >= 8:
        strength_score += 1
    if len(password) >= 12:
        strength_score += 1
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength_score += 1
    if re.search(r"\d", password):
        strength_score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1

    if strength_score <= 2:
        return "Weak"
    elif strength_score == 3 or strength_score == 4:
        return "Medium"
    else:
        return "Strong"

# Function triggered when the button is clicked
def on_check():
    password = entry.get()  # Get the input password
    if not password:
        messagebox.showwarning("Warning", "Please enter a password!")
        return

    strength = check_password_strength(password)
    messagebox.showinfo("Result", f"Password Strength: {strength}")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")  # Set window size

# Label
tk.Label(root, text="Enter Password:").pack(pady=5)

# Password Entry
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

# Check Button
tk.Button(root, text="Check Strength", command=on_check).pack(pady=10)

# Run the GUI
root.mainloop()
