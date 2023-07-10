"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO:
    """
    number = input('Secret number: ')
    secret_string = str(input('What\'s the ciphered string?'))
    print(secret_translate(number, secret_string))
    

def secret_translate(number, secret_string):
    """
    :param number: int, a number of user entered
    :param secret_string: str, a secret word and will be translated.
    """

    # step1. Change the word by user.
    new_alphabet = ''
    upper_secret_string = secret_string.upper()
    new_alphabet = ALPHABET[len(ALPHABET)-int(number):]
    new_alphabet = new_alphabet + ALPHABET[:len(ALPHABET)-int(number)]

    # step2. Translate the secret word! (secret_string)
    ans = ''
    for i in range(len(upper_secret_string)):
        if upper_secret_string[i] in new_alphabet:
            a = new_alphabet.find(upper_secret_string[i])
            ans += ALPHABET[a]
        elif ' ' in upper_secret_string[i]:
            ans += ' '
        else:
            ans += '!'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
