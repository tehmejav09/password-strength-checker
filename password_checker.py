"""
Password Strength Checker
A small tool that scores a password and explains why it's weak or strong.
Part of the Cipherora Projects series.
"""

# A short list of common passwords to catch obviously weak choices.
# In a real tool you'd load this from a much bigger file.
COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "password1", "111111", "letmein", "admin", "welcome"
}


def check_password(password):
    """Return a score (0-5) and a list of reasons explaining the score."""
    score = 0
    reasons = []

    # Rule 1: length
    if len(password) >= 12:
        score += 2
        reasons.append("Good length (12 or more characters).")
    elif len(password) >= 8:
        score += 1
        reasons.append("Acceptable length (8-11 characters), but longer is stronger.")
    else:
        reasons.append("Too short. Aim for at least 12 characters.")

    # Rule 2: character variety
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    variety = sum([has_lower, has_upper, has_digit, has_symbol])
    if variety >= 3:
        score += 2
        reasons.append("Mixes multiple character types (letters, numbers, symbols).")
    elif variety == 2:
        score += 1
        reasons.append("Uses only two character types. Add a symbol or a number.")
    else:
        reasons.append("Uses only one character type. This is easy to guess.")

    # Rule 3: not a known common password
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        reasons = ["This is one of the most commonly used passwords. "
                   "It would be guessed in seconds, regardless of length or symbols."]
    else:
        score += 1

    score = min(score, 5)
    return score, reasons


def label_for_score(score):
    labels = {
        0: "Very weak",
        1: "Weak",
        2: "Weak",
        3: "Okay",
        4: "Strong",
        5: "Very strong",
    }
    return labels[score]


if __name__ == "__main__":
    print("Password Strength Checker")
    print("Only checks the password locally. Nothing is sent anywhere.\n")

    pw = input("Enter a password to check: ")
    score, reasons = check_password(pw)

    print(f"\nScore: {score}/5 ({label_for_score(score)})")
    print("Why:")
    for r in reasons:
        print(f"  - {r}")
