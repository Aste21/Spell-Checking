from keyboard import *
from time import *
import os

word_dict = {}
file = open("words_alpha.txt", "r")
for word in file:
    word = word.strip()
    word_len = len(word)
    if word_len in word_dict:
        word_dict[word_len].append(word)
    else:
        word_dict[word_len] = [word]
file.close()


def lev(str1, str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    if str1[0] == str2[0]:
        return lev(str1[1:len(str1)], str2[1:len(str2)])
    return 1 + min(lev(str1[1:len(str1)], str2[1:len(str2)]), lev(str1[1:len(str1)], str2),
                   lev(str1, str2[1:len(str2)]))


def lev_miss_type(str1, str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    if str1[0] == str2[0] or is_miss_type(str1[0], str2[0]):
        return lev(str1[1:len(str1)], str2[1:len(str2)])
    return 1 + min(lev(str1[1:len(str1)], str2[1:len(str2)]), lev(str1[1:len(str1)], str2),
                   lev(str1, str2[1:len(str2)]))


def hamming(str1, str2):
    if len(str1) != len(str2):
        return -1
    count = 0
    for n in range(len(str1)):
        if str1[n] != str2[n]:
            count += 1
    return count


def hamming_miss_type(str1, str2):
    if len(str1) != len(str2):
        return -1
    count = 0
    for n in range(len(str1)):
        if str1[n] != str2[n] and not is_miss_type(str1[n], str2[n]):
            count += 1
    return count


def indel(str1, str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    if str1[0] == str2[0]:
        return indel(str1[1:len(str1)], str2[1:len(str2)])
    return 1 + min(indel(str1[1:len(str1)], str2), indel(str1, str2[1:len(str2)]))


def auto_correction(string, show_time):
    if show_time:
        start = time()
    f = open("words_alpha.txt", "r")
    word_corrected = string
    word_corrected_dist = 100000
    for line in f:
        word_f = str(line.strip())
        if len(word_f) == len(string):
            ham = hamming(string, word_f)
            if ham <= 1 and ham < word_corrected_dist:
                word_corrected = word_f
                word_corrected_dist = ham
    f.close()
    if show_time:
        end = time()
        print(f"Time of not optimized auto correction is: {end - start}")
    return word_corrected


def optimized_auto_correction(string, show_time):
    if show_time:
        start = time()
    global word_dict
    word_corrected = string
    word_corrected_dist = 100000
    if len(string) in word_dict:
        for word_f in word_dict[len(string)]:
            ham = hamming(string, word_f)
            if ham <= 1 and ham < word_corrected_dist:
                word_corrected = word_f
                word_corrected_dist = ham
    if show_time:
        end = time()
        print(f"Time of optimized auto correction is: {end - start}")
    return word_corrected


def file_editor(file_name_in):
    if os.path.exists("out.txt"):
        os.remove("out.txt")
    f = open(file_name_in, "r")
    g = open("out.txt", "x")
    is_first_line = True
    for line in f:
        is_first_word = True
        if not is_first_line:
            g.write("\n")
        is_first_line = False
        line = line.strip().split()
        for word_f in line:
            if not is_first_word:
                g.write(" ")
            g.write(optimized_auto_correction(word_f, False))
            is_first_word = False
    f.close()
    g.close()


x = input("Input string 1: ")
y = input("Input string 2: ")
z = input("Give me word to auto correct: ")
print(f"Levenshtein distance: {lev(x, y)}")
print(f"Hamming distance: {hamming(x, y)}")
print(f"InDel distance: {indel(x, y)}")
print(f"Levenshtein distance with miss type: {lev_miss_type(x, y)}")
print(f"Hamming distance with miss type: {hamming_miss_type(x, y)}")
print(auto_correction(z, True))
print(optimized_auto_correction(z, True))
file_editor("in.txt")
