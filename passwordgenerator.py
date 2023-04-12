import tkinter as tk
import random
import string

def generate_password():
    try:
        password_length = int(password_length_entry.get())
    except ValueError:
        password_label.config(text="Error: please enter a valid number for password length")
        return
    
    # Get the selected character sets
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_punctuation = punctuation_var.get()
    
    if not any([use_uppercase, use_lowercase, use_digits, use_punctuation]):
        use_uppercase = use_lowercase = use_digits = use_punctuation = True
    
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(password_length))
    
    password_label.config(text=password)

window = tk.Tk()
window.title("Password Generator")

password_length_label = tk.Label(window, text="Password Length:")
password_length_label.pack()
password_length_entry = tk.Entry(window)
password_length_entry.pack()

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(window, text="Uppercase Letters", variable=uppercase_var)
uppercase_checkbox.pack()

lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(window, text="Lowercase Letters", variable=lowercase_var)
lowercase_checkbox.pack()

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(window, text="Digits", variable=digits_var)
digits_checkbox.pack()

punctuation_var = tk.BooleanVar()
punctuation_checkbox = tk.Checkbutton(window, text="Punctuation", variable=punctuation_var)
punctuation_checkbox.pack()

generate_password_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_password_button.pack()

password_label = tk.Label(window, text="")
password_label.pack()

window.mainloop()
