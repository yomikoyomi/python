# -*- coding: utf-8 -*-

dict_1 = {"YEAR": "2015", "MONTH": "07", "DAY": "05"}

if __name__ == "__main__":
    print dict_1

    for key in dict_1:
        print key + " as ",
        print dict_1.get(key)
    print dict_1.has_key("YEAR")
    print "DAYS" in dict_1
    print "test"
