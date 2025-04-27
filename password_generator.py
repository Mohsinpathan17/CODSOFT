import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation
   characters = letters
    if use_digits:
        characters += digits
        
    if use_specials:
        characters += specials

    if not characters:
        return ''
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
if __name__ == "__main__":
    print("Generated password:", generate_password(length=16))
