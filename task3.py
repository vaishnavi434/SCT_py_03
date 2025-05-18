import re

def assess_password_strength(password):
    # Criteria checks
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[^A-Za-z0-9]', password))
    is_long_enough = len(password) >= 8

    # Count how many criteria are met
    score = sum([has_upper, has_lower, has_digit, has_special, is_long_enough])

    # Strength assessment
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Report
    print("\nPassword Strength Report:")
    print(f" - Length >= 8 characters: {'✅' if is_long_enough else '❌'}")
    print(f" - Contains uppercase letter: {'✅' if has_upper else '❌'}")
    print(f" - Contains lowercase letter: {'✅' if has_lower else '❌'}")
    print(f" - Contains digit: {'✅' if has_digit else '❌'}")
    print(f" - Contains special character: {'✅' if has_special else '❌'}")
    print(f"\nOverall Strength: {strength}")

# Main block for command-line use
if __name__ == "__main__":
    while True:
        pwd = input("\nEnter a password to assess (or type 'exit' to quit): ")
        if pwd.lower() == 'exit':
            break
        assess_password_strength(pwd)
