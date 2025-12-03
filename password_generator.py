import string
import secrets

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Generate a strong, secure password using Python's secrets module."""

    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


# --- CLI Interface ---
if __name__ == "__main__":
    print("\n🔐 Secure Password Generator")
    
    try:
        length = int(input("Enter password length (default = 16): ") or 16)

        print("\nChoose character types (y/n):")
        use_upper = input("Include uppercase letters? ").lower() == 'y'
        use_lower = input("Include lowercase letters? ").lower() == 'y'
        use_digits = input("Include digits? ").lower() == 'y'
        use_symbols = input("Include symbols? ").lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        
        print("\n✅ Your Secure Password:")
        print(password)

    except ValueError:
        print("\n❌ Invalid input. Please enter a valid number.")
