"""
File: anagram.py
Name: Steven
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
EARLY_STOPPING = 2

def main():
    """
    TODO:
    """
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    s = str(input('Find anagram for: '))
    while True:
        if s == EXIT:
            break
        else:
            start = time.time()

            d_s = {}  # 先針對使用者輸入的str轉換成dic, 給後面base_case_check使用
            for ch in s:
                if ch not in d_s:
                    d_s[ch] = 1
                else:
                    d_s[ch] += 1

            words = {}
            read_dictionary(FILE, words, s)  # 把字典的資訊轉換成dic
            find_anagrams(d_s, s, words)  # 開始recursion

            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')
            s = str(input('Find anagram for: '))


def read_dictionary(filepath, words, s):
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            ans = 0
            for ch in line:
                if ch in s:
                    ans += 1
            if ans == len(line):
                words[line] = 1


def find_anagrams(d_s, s, words):
    """
    :param s: str, 使用者輸入的單字
    :return: list, return使用者輸入單字的排列組合，且是有意義的單字
    """
    print('Searching...')
    ans = []

    all_word = find_anagrams_helper(d_s, s, '', words, [])  # 利用recursion抓出有可能是單字的各種排列list
    print(len(all_word))
    for word in all_word:  # 將有可能是單字的排列list, 與字典進行比對；如果是單字，則加入ans的list內
        if word in words:
            ans.append(word)
            print('Found: ', word)  # 如果有找到單字，就print出來
            print('Searching...')
    print(len(ans), 'anagrams: ', ans)  # 輸出答案到console


def find_anagrams_helper(d_ans, enter_s, current_s, words, ans_lst):
    """
    basecase設定的條件如下：
    1. recursion排列後的str字母長度要等於使用者輸入的字母長度
    2. recursion排列的字母數量與使用者輸入的字母數量要一致
    3. 排除有相同排列str
    """

    if len(current_s) == len(enter_s):  # Base case條件之一, 先讓recursion抓出與使用者輸入字元一樣的長度
        if base_case_check(current_s, d_ans, ans_lst):  # 另外寫function確認base case條件是否都有達到，如果有就回傳True
            ans_lst.append(current_s)
    else:
        for s in enter_s:
            # early stopping
            if len(current_s) == EARLY_STOPPING:  # 只抓取字串長度==2時進入early stopping
                if has_prefix(current_s, words):
                    break
            # choose
            current_s += s

            # explore
            find_anagrams_helper(d_ans, enter_s, current_s, words, ans_lst)

            # un-choose
            current_s = current_s[:len(current_s)-1]
    return ans_lst


def base_case_check(current_s, d_ans, ans_lst):
    d_s = {}
    for s in current_s:  # 把recursion排列的str轉換成dic
        if s in d_s:
            d_s[s] += 1
        else:
            d_s[s] = 1

    if d_s == d_ans:  # 比對使用者的dic以及recursion的dic
        if current_s not in ans_lst:  # 排除重覆的
            return True
    return False


def has_prefix(sub_s, words):
    """
    :param sub_s: str, 當下recursion排列的str
    :return: boolean, 會比對sub_s在字典內是否有對應開頭的單字，有就回傳true
    """
    for word in words:
        if word.startswith(sub_s):
            return False
    return True


if __name__ == '__main__':
    main()
