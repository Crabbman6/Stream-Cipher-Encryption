import random
import string 

def stream_cipher(message):
    # Prompt the user to enter a seed key
    seedkey = input("Please enter your seed key as a digit")
    # Use the seed key to initialize the random number generator
    random.seed(seedkey)
    # Generate a random key of the same length as the message
    key = ''.join(random.choices(string.ascii_letters, k=len(message)))
    # Get the length of the message
    messagelen = len(message)
    # Convert the message into a list of characters
    characterlist = []
    for char in message:
        characterlist.append(char)

    # Initialize an empty output string
    output_string = ""
    # Iterate through the message, one character at a time
    for i in range(messagelen):
        # Get the current character and the corresponding key character
        curr_character = characterlist[i]
        curr_key = key[i%len(key)]
        # XOR the current character and key character, and add the result to the output string
        output_string = output_string + chr(ord(curr_character) ^ ord(curr_key))

    # Print the encrypted message
    print("Encoded message is ", output_string)
    # Return the encrypted message and the key
    return output_string, key

def decode_message(encrypted_message, key):
    # Initialize an empty output string
    output_string = ""
    # Iterate through the encrypted message, one character at a time
    for i in range(len(encrypted_message)):
        # Get the current character and the corresponding key character
        curr_character = encrypted_message[i]
        curr_key = key[i]
        # XOR the current character and key character, and add the result to the output string
        output_string = output_string + chr(ord(curr_character) ^ ord(curr_key))

    # Return the decrypted message
    return output_string


# Test the stream cipher
message = "House on the hill"
encrypted_message, key = stream_cipher(message)
decrypted_message = decode_message(encrypted_message, key)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)