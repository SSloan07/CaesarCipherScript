from .Utils.alphabet import (
    alphabet_spanish,
    alphabet_spanish_inv,
    alphabet_english,
    alphabet_english_inv
)

from .Core.encryption import encryption
from .Core.decryption import decryption
from .Utils.invalid_type import valid_type

print("Welcome to our Caesar Cipher")

while True:
    # Info from user

    option = valid_type("\nMenu\n1) Encryption\n2) Decryption\nChoose an option: ",(1, 2))
    language_option = valid_type("\nChoose a language\n1) Spanish\n2) English\nChoose an option: ",(1, 2))
    message = input("\nIntroduce your message: ")
    key = valid_type("\nIntroduce your key: ")


    # Validate alphabet
    if language_option == 1:
        selected_alphabet = alphabet_spanish
        selected_alphabet_inv = alphabet_spanish_inv
    else:
        selected_alphabet = alphabet_english
        selected_alphabet_inv = alphabet_english_inv

    # Validate Operation
    if option == 1:
        result = encryption(message,key,selected_alphabet,selected_alphabet_inv)
        print(f"\nYour encrypted message is: {result}")
    else: 
        result = decryption(message,key,selected_alphabet,selected_alphabet_inv)
        print(f"\nYour decrypted message is: {result}")
    

    # Ask if wanna do anything more

    option_activity = valid_type("\nWould you like to do anything else?\n1) Yes\n2) No\nChoose an option: ",(1,2))
    
    if option_activity == 2:
        print("Goodbye!")
        break

    continue 
        