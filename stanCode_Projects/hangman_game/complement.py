"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    TODO:
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :param dna:uppercase letter, the user enter word that must was uppercase letter.
    """
    ans = ''
    if dna.isupper():
        a = 0
        for i in range(len(dna)):
            if dna[a] == 'A':
                ans += 'T'
            elif dna[a] == 'T':
                ans += 'A'
            elif dna[a] == 'G':
                ans += 'C'
            else:
                ans += 'G'
            a += 1
    else:
        ans = 'DNA strand is missing'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
