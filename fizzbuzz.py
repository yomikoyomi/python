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

if __name__ == "__main__":
    for i in range(1, 101):
        print(fizzbuzz(i))
