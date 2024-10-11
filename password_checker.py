import re

def password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password)
    uppercase_criteria = re.search(r'[A-Z]', password)
    number_criteria = re.search(r'[0-9]', password)
    special_char_criteria = re.search(r'[\W_]', password)

    # Calculate score
    score = sum([length_criteria, bool(lowercase_criteria), bool(uppercase_criteria), bool(number_criteria), bool(special_char_criteria)])

    # Feedback
    feedback = []
    if not length_criteria:
        feedback.append("- Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("- Include lowercase letters.")
    if not uppercase_criteria:
        feedback.append("- Include uppercase letters.")
    if not number_criteria:
        feedback.append("- Include at least one number.")
    if not special_char_criteria:
        feedback.append("- Include special characters (e.g. !@#$%^&*).")

    # Determine strength
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Output
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(suggestion)

# Example usage
password = input("Enter your password: ")
password_strength(password)
