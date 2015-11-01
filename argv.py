# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    param = sys.argv
    obj = open("test.txt", "w")
    for value in range(100):
        print >> obj, value

        if value == 20:
            print >> obj, u"for roop is 20 over!!"
            sys.exit()
