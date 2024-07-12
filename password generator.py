import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1"
    
    # Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        # Get user input for password length
        length = int(input("Enter the desired length of the password: "))
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
