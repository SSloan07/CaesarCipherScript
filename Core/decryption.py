def decryption (message, key, alphabet, alphabet_inv): 
    movement = key % len(alphabet)
    decrypted_message =""
    for i in range(len(message)): 
        if message[i] in alphabet: 
            original_index_alph = alphabet[message[i]]
            decrypted_message += alphabet_inv[(original_index_alph - movement)%len(alphabet)]
        else: 
            decrypted_message += message[i]

    return decrypted_message

