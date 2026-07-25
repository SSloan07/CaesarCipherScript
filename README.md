# CaesarCipherScript

## Overview

CaesarCipherScript is a Python command-line application that allows users to encrypt and decrypt messages using the Caesar cipher. The user can choose the operation, select an English or Spanish alphabet, and provide a positive numeric key.

The application preserves spaces, numbers, punctuation marks, and characters that are not part of the selected alphabet. Messages are converted to lowercase before encryption.

## How to run

Make sure Python 3 is installed, then run the following commands from the project directory:

```bash
cd CaesarCipherScript
python script.py
```

The application will ask the user to:

1. Choose between encryption and decryption.
2. Select English or Spanish.
3. Enter the message.
4. Enter a positive numeric key.

## Technical documentation

Detailed technical documentation and Mermaid diagrams are available in the [`documentation`](Documentation/README.md) folder.

## Reference resource

The following video was used as a learning reference for the Caesar cipher algorithm and its implementation:

- [Caesar cipher implementation reference video](https://www.youtube.com/watch?v=DT3bsFpuikY)

## Tests performed

The following tests verify the main workflow and the input validation implemented in the application.

### 1. Complete encryption and decryption workflow

**Question:** Can the application encrypt a message and then decrypt the resulting ciphertext using the same key?

<img width="1913" height="949" alt="Encryption workflow" src="https://github.com/user-attachments/assets/2bd72739-f5e2-46f9-a5d2-a2c4b3c6f228" />

<img width="1913" height="958" alt="Decryption workflow" src="https://github.com/user-attachments/assets/8163a4f8-b19d-4fd5-8427-67a1acb5846b" />

The complete workflow works correctly: the application encrypts the original message with the selected key, and decrypting the ciphertext with the same key recovers the original message.

### 2. Invalid menu option

**Question:** What happens if the user enters a menu option that does not exist?

<img width="1911" height="473" alt="Invalid menu option" src="https://github.com/user-attachments/assets/bd9356f0-b022-4ede-b11a-3b2aaaf22978" />

The application displays an invalid-option message and does not continue until the user enters one of the available options.

### 3. Characters not included in the selected alphabet

**Question:** What happens if the message contains a character that is not part of the selected alphabet?

<img width="1911" height="578" alt="Characters outside the selected alphabet" src="https://github.com/user-attachments/assets/d90f73db-c96d-45b5-af4d-d0b8b44b1e30" />

The application does not crash. Characters such as spaces, numbers, and punctuation are preserved unchanged, which is expected behavior for this Caesar cipher implementation.

### 4. Text entered where a number is expected

**Question:** What happens if the user enters text in a numeric prompt?

<img width="1913" height="916" alt="Text entered in a numeric prompt" src="https://github.com/user-attachments/assets/54128d26-8ec1-449b-a8ca-7e9064f0c831" />

The application rejects the input, displays an error message, and asks the user to enter an integer before continuing.

### 5. Non-numeric key

**Question:** What happens if the user enters text instead of a numeric key?

<img width="1913" height="733" alt="Non-numeric key" src="https://github.com/user-attachments/assets/f78e9b02-eeed-411a-abfb-80d20d5d84ec" />

The application rejects the key because it is not an integer and asks the user to enter a numeric value.

### 6. Negative key

**Question:** What happens if the user enters a negative integer as the key?

<img width="1913" height="733" alt="Negative key" src="https://github.com/user-attachments/assets/ca2e82d0-7757-4ad4-8606-2edd293ed56a" />

The application rejects the negative key because keys must be strictly positive. It displays an error message and asks the user to enter a positive integer.
