#!/usr/bin/python3

import random
import sys

key = {
    0: ['A'],
    1: ['A#', 'Bb'],
    2: ['B'],
    3: ['C'],
    4: ['C#', 'Db'],
    5: ['D'],
    6: ['D#', 'Eb'],
    7: ['E'],
    8: ['F'],
    9: ['F#', 'Gb'],
    10: ['G'],
    11: ['G#', 'Ab']
}

base = {
    6: 7,
    5: 0,
    4: 5,
    3: 10,
    2: 2,
    1: 7,
}


def get_notename(string, fret):
    return key[(base[string]+fret) % 12]


def main():
    string = int(input("今天要练哪根弦?(输入0则弦数随机):"))
    
    random_flag = False
    if string == 0:
        random_flag = True
    while True:
        if random_flag:
            string = random.randint(1, 6)
        fret = random.randint(0, 12)

        ip = input("{} 弦 {} 品 :".format(string, fret))
        ans = get_notename(string, fret)
        if ip in ans:
            print("bingo!")
        else:
            if len(ans) == 1:
                print("额~ 应该是{}".format(ans[0]))
            else:
                print("额~ 应该是{} 或 {}".format(ans[0], ans[1]))


if __name__ == "__main__":
    main()
