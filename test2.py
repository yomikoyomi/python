# -*- coding: utf-8 -*-

import datetime

if __name__ == "__main__":
    today = datetime.date.today()
    todaydetail = datetime.datetime.today()

    # today
    print today
#    print todaydetail
#
#    print "--------------------"
#    print today.year
#    print today.month
#    print today.day
#    print todaydetail.year
#    print todaydetail.month
#    print todaydetail.day
#    print todaydetail.hour
#    print todaydetail.minute
#    print todaydetail.second
#    print todaydetail.microsecond
#
#    print "--------------------"
#    print today.isoformat()
#    print todaydetail.strftime("%Y/%m/%d %H:%M:%S")
    print today + datetime.timedelta(days=1)
    newyear = datetime.datetime(2015,1,1)

    ## 2016年1月1日の1週間後
    print newyear + datetime.timedelta(days=7)
    
    calc = todaydetail - newyear
    print calc.days

