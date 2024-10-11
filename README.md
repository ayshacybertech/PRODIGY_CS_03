# Password Complexity Checker

This project is a Python-based tool that assesses the strength of a password based on various criteria, including length, uppercase and lowercase letters, numbers, and special characters. It provides feedback on whether the password is **Weak**, **Moderate**, or **Strong**.

## Features

- **Password Length:** Ensures the password has at least 8 characters.
- **Uppercase Letters:** Checks if the password contains uppercase letters (A-Z).
- **Lowercase Letters:** Checks if the password contains lowercase letters (a-z).
- **Numbers:** Verifies if the password includes numeric digits (0-9).
- **Special Characters:** Ensures the inclusion of special characters (e.g., `!@#$%^&*()`).

## How It Works

The script evaluates the password based on the following five criteria:

1. **Length:** The password must be at least 8 characters long.
2. **Uppercase Letters:** At least one uppercase letter (A-Z).
3. **Lowercase Letters:** At least one lowercase letter (a-z).
4. **Numbers:** At least one number (0-9).
5. **Special Characters:** At least one special character (e.g., `!@#$%^&*()`).

The password's strength is classified as:
- **Weak:** Meets fewer than 3 of the criteria.
- **Moderate:** Meets at least 3 criteria.
- **Strong:** Meets all 5 criteria.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:ayshacybertech/PRODIGY_CS_03.git

2.Navigate to the Project Directory:
cd PRODIGY_CS_03

3.Run the Script:
python3 password_checker.py

4.Enter a Password: After running the script, you will be prompted to enter a password, and the tool will provide feedback on its strength.
