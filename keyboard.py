from math import *

keyboard = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
            ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
            ["z", "x", "c", "v", "b", "n", "m"]]


def get_key_position(key):
    global keyboard
    for y in range(len(keyboard)):
        for x in range(len(keyboard[y])):
            if key == keyboard[y][x]:
                return [x, y]
    return -1


def key_distance(key1, key2):
    key1_cord = get_key_position(key1)
    key2_cord = get_key_position(key2)
    return sqrt(pow(key1_cord[0] - key2_cord[0], 2) + pow(key1_cord[1] - key2_cord[1], 2))


def is_miss_type(key1, key2):
    if key_distance(key1, key2) <= 1:
        return True
    return False
