def encryption (message, key, alphabet, alphabet_inv): 
    message = message.lower()
    movement = key % len(alphabet)
    encripted_message = ""
    for i in range(len(message)): 
        if message[i] in alphabet:
            original_index_alph = alphabet[message[i]]
            encripted_message += alphabet_inv[(original_index_alph + movement)%len(alphabet)]
        else: 
            encripted_message += message[i]
    return encripted_message

