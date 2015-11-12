#! -*- coding: utf-8 -*-

def fizzbuzz(num):
    FIZZ = 3
    BUZZ = 5

    if num % FIZZ == 0 and num % BUZZ == 0:
        return "FIZZBUZZ"
    elif num % FIZZ == 0:
        return "FIZZ"
    elif num % BUZZ == 0:
        return "BUZZ"
    else:
        return num

def fizzbuzz2(num):
    FIZZ = 3
    BUZZ = 5
    fizBuz=""

    if num % FIZZ != 0 and num % BUZZ != 0:
        return num
    if num % FIZZ == 0:
        fizBuz = fizBuz + "fizz"
    if num % BUZZ == 0:
        fizBuz = fizBuz + "buzz"
    return fizBuz

def fizzbuzz3(num):
    if(num%15 == 0):
        return 'fizzbuzz'
    elif(num%5 == 0):
        return 'buzz'
    elif(num%3 == 0):
        return 'fizz'
    else:
        return ''
if __name__ == "__main__":
    for i in range(1, 101):
        print(i)
        print(fizzbuzz3(i))
