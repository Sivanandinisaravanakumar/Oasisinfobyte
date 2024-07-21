import random
import string

def get_user_input():
    """Get password length and character set preferences from the user and validate the input."""
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                raise ValueError("Password length must be a positive number.")
            
            include_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
            include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
            include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
            
            if not (include_letters or include_numbers or include_symbols):
                raise ValueError("At least one character type must be selected.")
            
            return length, include_letters, include_numbers, include_symbols
        except ValueError as e:
            print(e)
            print("Please enter valid inputs.")

def generate_password(length, include_letters, include_numbers, include_symbols):
    """Generate a random password based on user-defined criteria."""
    character_set = ""
    if include_letters:
        character_set += string.ascii_letters
    if include_numbers:
        character_set += string.digits
    if include_symbols:
        character_set += string.punctuation
    
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length, include_letters, include_numbers, include_symbols = get_user_input()
    password = generate_password(length, include_letters, include_numbers, include_symbols)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
