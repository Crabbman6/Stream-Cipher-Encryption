# Stream-Cipher-Encryption

This repository contains a Python implementation of a simple stream cipher for encrypting and decrypting messages. 

## Features

The script contains two functions:

- `stream_cipher`: This function prompts the user for a seed key, generates a random key of the same length as the message, and then XORs each character of the message with the corresponding character of the key to encrypt the message.

- `decode_message`: This function takes an encrypted message and a key, and then XORs each character of the encrypted message with the corresponding character of the key to decrypt the message.

## Usage

To use the script, call the `stream_cipher` function with a message as argument. This will return the encrypted message and the key. Then, call the `decode_message` function with the encrypted message and the key to decrypt the message.
