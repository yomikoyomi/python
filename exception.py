# --*-- coding: utf-8 --*--

import sys
import traceback

def exception_test(num1, num2):
    print "==========計算開始=========="

    result = 0

    try:
        result = num1 + num2
    except:
        print "例外発生!"
        raise
    finally:
        print "計算終了!!"
    return result

def calc(num_list1, num_list2):
    try:
        print exception_test(num_list1[0], num_list2[0])
        print exception_test(num_list1[1], num_list2[1])
        print exception_test(num_list1[2], num_list2[2])
    except:

        print "例外を受け取りました"
        print traceback.format_exc(sys.exc_info()[2])

if __name__ == "__main__":
    num_list1 = [100, 200, 300]
    num_list2 = [100, 200, "300"]
    calc(num_list1, num_list2)
