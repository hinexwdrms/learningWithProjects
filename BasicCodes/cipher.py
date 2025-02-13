# This program encrypts and decrypts a message using the Vigenere cipher
custom_key = input('Enter the custom key: ').lower()
print("\nWould you like to encrypt or decrypt a message?")
choice = input("\nEnter 'e' for encrypt or 'd' for decrypt: ").lower()

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)] #prevents error if key < message [keeps looping]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    print(f'\nKey: {custom_key}')
    return vigenere(message, key)
    
def decrypt(message, key):
    print(f'\nKey: {custom_key}')
    return vigenere(message, key, -1)

if choice == 'e':
    text = input('Enter the text to encrypt: ')
    encryption = encrypt(text, custom_key)
    print(f'\nEncrypted text: {encryption}')
elif choice == 'd':
    text = input('Enter the text to decrypt: ')
    decryption = decrypt(text, custom_key)
    print(f'\nDecrypted text: {decryption}\n')
else:
    print('Invalid choice.')


