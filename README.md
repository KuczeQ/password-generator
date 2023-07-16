# Password Generator

This is a simple password generator application implemented using the Tkinter library in Python. The application allows the user to generate random passwords with various configurations.

## Prerequisites
- Python 3.x
- Tkinter library

## How to Run
1. Install Python 3.x if you haven't already.
2. Install the Tkinter library if it's not already included with your Python installation.
3. Save the code in a file with a `.py` extension (e.g., `password_generator.py`).
4. Open a terminal or command prompt and navigate to the directory where the file is saved.
5. Run the script using the command `python password_generator.py`.

## Usage
1. Enter the desired password length in the "Password Length" entry field.
2. Select the character sets to include in the password by checking the corresponding checkboxes:
   - "Uppercase Letters": Includes uppercase letters (A-Z).
   - "Lowercase Letters": Includes lowercase letters (a-z).
   - "Digits": Includes numeric digits (0-9).
   - "Punctuation": Includes punctuation characters.
3. Click the "Generate Password" button to generate a random password based on the selected options.
4. The generated password will be displayed in the label below the button.
5. Click the "Copy Password" button to copy the generated password to the clipboard. A message box will confirm the successful copy operation.

Note: If no character sets are selected, all character sets (uppercase letters, lowercase letters, digits, and punctuation) will be included by default.

## Error Handling
- If an invalid number is entered for the password length, an error message will be displayed in the label, and no password will be generated.
