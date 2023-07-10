"""
File: babynames.py
Name: Steven
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    # 先做字串的處理，利用.strip()去除字串的前後的空白以及換行符號
    year = year.strip()
    name = name.strip()
    rank = rank.strip()

    # 先判斷名字有沒有在dict, 如果沒有直接加入
    if name not in name_data:
        name_data[name] = {year: rank}
    else:
        # 如果有名字在dict, 確認年份有沒有重覆, 沒有的話直接加入；有的話再確認rank大小，如果排名比較前面則加入dict
        if year in name_data[name]:
            if int(rank) < int(name_data[name][year]):
                name_data[name][year] = rank
        else:
            name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    get_year = True  # 開關

    with open(filename, 'r') as f:
        for line in f:
            tokens = line.split(',')
            if get_year:  # 因為每個檔案的第一行都是年份，因此先取得年份後，再取rank
                year = tokens[0]  # 抓取year
                get_year = False
            else:
                rank = tokens[0]  # 抓取rank
                boy_baby_name = tokens[1]  # 抓取男寶寶的名字
                girl_baby_name = tokens[2]  # 抓取女寶寶的名字

                # 將year, rank, name丟入function add_data_for_name
                add_data_for_name(name_data, year, rank, boy_baby_name)
                add_data_for_name(name_data, year, rank, girl_baby_name)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}  # 製造空dict
    for filename in filenames:
        add_file(name_data, filename)

    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    names = []
    for name in name_data:
        if target.lower() in name.lower():
            names.append(name)

    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
