# -*- coding: utf-8 -*-

class ExtList(list):
    def __init__ (self):
        list.__init__(self)

    def append(self, value):
        list.append(self, value)
        print "値が追加されました: " + str(value)

if __name__ == "__main__":
    test = ExtList()
    test.append("TEST")
    test.append("-")
    test.append("test")

    print "---------------"
    for val in test:
        print val
