"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO:
    """
    a = ''
    answer = random_word()
    for i in range(len(answer)):
        a += '-'
    print('The word looks like ' + a)
    n_turns = N_TURNS
    old_ans = ''

    while n_turns > 0:  # Do the first string.
        print('You have '+str(n_turns)+' wrong guesses left.')
        a = input('Your guess:')
        input_ch = a.upper()

        if str.isalpha(input_ch) != 1:
            print('Illegal format')
        elif len(input_ch) > 1:
            print('Illegal format')
        else:
            if input_ch in answer:
                print('you are correct!')
                old_ans = ch_check_0(answer, input_ch, old_ans)  # Use ch_check_0 function got the first string.
                print('The word looks like ' + old_ans)
                break
            else:
                n_turns -= 1
                print('There is no ' + input_ch + '\'s in the word.')

    while n_turns > 0:  # After first string, compute every string
        print('You have ' + str(n_turns) + ' wrong guesses left.')
        a = input('Your guess:')
        input_ch = a.upper()

        if str.isalpha(input_ch) != 1:
            print('Illegal format')
        elif len(input_ch) > 1:
            print('Illegal format')
        else:
            if input_ch in answer:
                print('you are correct!')
                old_ans = ch_check_1(answer, input_ch, old_ans)  # Use ch_check_1 got the string after first.
                if old_ans.isalpha():
                    break
            else:
                n_turns -= 1
                print('There is no ' + input_ch + '\'s in the word.')
        print('The word looks like ' + old_ans)

    if n_turns > 0:  # print the final result.
        print('You win!!')
    else:
        print('You are completely hung :(')
    print('The word was: ' + answer)


def ch_check_0(answer, input_ch, old_ans):
    """
    :param answer: str, a random key word that was be guessed by player
    :param input_ch: str, a word by player guess
    :param old_ans: str, store the first string
    """
    for i in range(len(answer)):
        if answer[i] == input_ch:
            old_ans += input_ch
        else:
            old_ans += '-'
    return old_ans


def ch_check_1(answer, input_ch, old_ans):
    """
    :param answer: str, a random key word that was be guessed by player
    :param input_ch: str, a word by player guess
    :param old_ans: str, store every string
    """
    ans = ''
    for i in range(len(answer)):
        if answer[i] == input_ch:
            ans += input_ch
        elif answer[i] == old_ans[i]:
            ans += old_ans[i]
        else:
            ans += '-'

    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
