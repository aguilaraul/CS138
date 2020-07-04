#
# author    Raul Aguilar
# date      July 3, 2020
#
# CS 138 1535 Midterm Project 2
# Write a program that can encode and decode Caesar ciphers.
#
# Algorithm:
# Ask for user input
# Retreive message, shift, and choice of encryption or decryption
# For every letter in the message
#  Check if it is a letter
#   If it is a letter, check if encrypting or decrypting
#    If encrypting, add shift to the letter
#    If decrypting, subtract shift from letter
#   If the letter is lowercase:
#    If letter is shifted past z, subtract from alphabet to wrap around
#    If letter is shifted past a, add to alphabet to wrap back
#   If the letter is uppercase:
#    Repeat process for lowercase but with uppercase characters
#  If it is not a letter
#   Symbols and numbers do not get shifted
# Return cipher


def caesarCipher(str, shift, encrypt):
    if shift > 26:
        shift = shift%26

    cipher = []
    for ch in str:
        if ch.isalpha():
            if encrypt:
                ch = chr(ord(ch)+shift)
            else:
                ch = chr(ord(ch)-shift)

            if ch.islower():
                if ch > "z":
                    cipher.append(chr(ord(ch - (26-shift))))
                elif ch < "a":
                    cipher.append(chr(ord(ch + (26+shift))))
                else:
                    cipher.append(ch)
            elif ch.isupper():
                if ch > "Z":
                    cipher.append(chr(ord(ch - (26-shift))))
                elif ch < "A":
                    cipher.append(chr(ord(ch + (26+shift))))
                else:
                    cipher.append(ch)
        else:
            cipher.append(ch)
                    
    return "".join(cipher)
    

def main():
    quitEntry = False

    while not quitEntry:
        validEntry = False
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Quit")
        
        while not validEntry:
            try:
                choice = int(input("Enter an option: "))
                if choice in [1, 2, 3]:
                    validEntry = True
                else:
                    print("Enter a valid option")
            except:
                print("Enter a valid option")

        if choice == 1:
            message = input("Enter a message to encrypt: ")
            shift = int(input("Enter the shift to use: "))
            encrypted = caesarCipher(message, shift, True)
            print("Message:")
            print(message)
            print("Encryption:")
            print(encrypted)
        elif choice == 2:
            message = input("Enter a message to decrypt: ")
            shift = int(input("Enter the shift used: "))
            decrypted = caesarCipher(message, shift, False)
            print("Message:")
            print(message)
            print("Decryption:")
            print(decrypted)
        else:
            quitEntry = True
        print()


main()
