# -*- coding: utf-8 -*-

class test ():
    def __init__(self, name, value):
        self.name = name
        self.value = value

if __name__ == "__main__":
    classList = []
    classList.append(test("てすと1", "test"))
    classList.append(test("test2", "aaaaa"))

    for testClass in classList:
        print "==========START============="
        print "name ===> " + testClass.name
        print "value ===> " + testClass.value
        
