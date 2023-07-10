"""
File: similarity.py (extension)
Name:
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO:
    """
    long_seq = input('Please give me a DNA sequence to search: ').upper()
    short_seq = input('What DNA sequence would you like to match?').upper()
    print('The best match is ' + homology(long_seq, short_seq))


def homology(long_seq, short_seq):
    new_ans = 0
    ch = ''
    for i in range(len(long_seq)-len(short_seq)+1):
        a = 0
        for j in range(len(short_seq)):
            if long_seq[j+i] == short_seq[j]:
                a += 1
        ans = a / len(short_seq)
        if ans > new_ans:
            new_ans = ans
            ch = long_seq[i:i+len(short_seq)]
    return ch


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
