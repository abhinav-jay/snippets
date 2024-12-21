import matplotlib.pyplot as plt
import time
import math


def factor(n):
    global s
    s = 0
    i = 2
    r = math.sqrt(n)
    while i < r:
        if n % i == 0:
            s += i
            s += n / i
            i += 1
        else:
            i += 1

    s += 1


ls = []

def main(n):
    global ls
    k = 0

    ls.append(math.log(n))
    while k < 200:
        factor(n)
        n = s
        k += 1
        ls.append(math.log(n))
        if n == 1:
            break
    return ls
    print(ls)


def plot():

    n = int(input("enter the first number of the sequence"))
    start = time.time()
    main(n)

    end = time.time()
    t = end - start
    print(t, "seconds")

    plt.plot(ls)
    plt.xlabel("aliquiot sequence of the number")
    plt.show()


plot()
