import random
import pyperclip
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/~`"
def generate_password(length):
    """Generate a random password of specified length."""
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    password = []
    password.append(random.choice("abcdefghijklmnopqrstuvwxyz"))  
    password.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  
    password.append(random.choice("0123456789"))                  
    password.append(random.choice("!@#$%^&*()_+-=[]{}|;:',.<>?/~`"))  
    for _ in range(length - 4):
        password.append(random.choice(characters))

    random.shuffle(password)  
    pyperclip.copy(''.join(password))
    print("Password copied to clipboard.")
    return ''.join(password)  

print(generate_password(length=12))