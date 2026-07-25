from .alphabet import (
    alphabet_spanish,
    alphabet_spanish_inv,
    alphabet_english,
    alphabet_english_inv
)

from .Core.encryption import encryption
from .Core.decryption import decryption


print("Welcome to our Caesar Cipher")

while True:
    # Info from usser
    option = int(input("\nMenu\n1) Encryption\n2) Decryption\nChoose an option: "))
    language_option = int(input("\nChoose a language for the message\n1) Spanish\n2) English\nChoose an option: "))
    message = input("\nIntroduce your message: ")
    key = int(input("\nIntroduce your key: "))

    # Validate alphabet
    if language_option == 1:
        selected_alphabet = alphabet_spanish
        selected_alphabet_inv = alphabet_spanish_inv
    elif language_option == 2:
        selected_alphabet = alphabet_english
        selected_alphabet_inv = alphabet_english_inv
    else:
        print("Invalid language option.")
        continue

    # Validate Operation
    if option == 1:
        result = encryption(message,key,selected_alphabet,selected_alphabet_inv)
        print(f"\nYour encrypted message is: {result}")
    elif option == 2:
        result = decryption(message,key,selected_alphabet,selected_alphabet_inv)
        print(f"\nYour decrypted message is: {result}")
    else:
        print("Invalid operation.")
        continue

    # Ask if wanna do anything more


    option_activity = int(input("\nWould you like to do anything else?\n1) Yes\n2) No\nChoose an option: \t"))

    while(option_activity > 2 or option_activity <1): 
        option_activity =int(input("\nInvalid Option. Remember: \n\n1) Yes\n2) No\n"))

    if option_activity == 2:
        print("Goodbye!")
        break

    continue 
        