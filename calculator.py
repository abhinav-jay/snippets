import math
import random


def lowest_common_multiple ():
    n = int(input("enter the first number:"))
    a = int(input("enter the second number"))
    if n > a:
        big = n
    elif a == n:
        print("both number are the same")
        exit(0)
    else:
        big = a
    while 1:
        if (big % n) == 0 and (big % a) == 0:
            print("The LCM of",a,"and",n,"is",big)
            break
        else:
            big += 1




def game():
    n = random.randrange(1, 1000)
    q = input("do you want to quit?:")
    if q == "no":
        while 1:
            t = int(input("enter a number:"))
            if t == n:
                print("great job")
                break
            elif t > n:
                print("the number is smaller")
            elif t < n:
                print("the number is bigger")
    else:
        exit(0)


def ballheight():
    r = int(input("1:fact\n2:prewiew\n:"))
    if r == 1:
        t = float(input("enter the time(s):"))
        a = float(input("enter the accelaration(m/s)(earth=9.8):"))
        s = (1/2*a*(t/2)**2)
        m = t/2*9.8
        k = m*3.6
        print(" \nit went to a height of", s ,"meters\n  ")
        print(" \nyou threw it at a speed of",m,"m\s,or",k,"kph,or",k/1.6,"mph\h ")
    elif r == 2:
        h = float(input("enter the height:"))
        ea = str(input("are you on earth?[y/n]:"))
        v = 9.8*(((2*h)/9.8)**0.5)
        if ea == "y":
            print(" \nyou will have to throw it at a speed of",v*3.6,"kph\n ")
        else:
            print("sorry,we can't help you")





def conv():
    l = float(input("enter the length(m):"))
    t = float(input("enter the time(s):"))
    a = (l/t)*3.6
    print("\nthe speed is:",a,"kph, or we can also say",a/1.6, "mph\n ")



def prism():
    ip = int(input("enter the base's number of sides:"))
    i = int(input("enter the height:"))
    if ip == 3:
        it = int(input("enter the base's base:"))
        h = int(input("enter the base's height:"))
        print("   \nit's volume is equal to" , ((it*h)/2)*i , "units cubed\n    ")
    elif ip == 4:
        l = int(input("enter base's length:"))
        w = int(input("enter base's width:"))
        print(" \nit's volume is equal to" , l * w *i , "units cubed\n  ")
    elif ip == 5:
        p = int(input("enter it's perimeter:"))
        a = int(input("enter it's apothem:"))
        print(" \nit's volume is equal to" , 0.5*p*a*i , "units cubed\n    ")
    elif ip == 6:
        s = int(input("enter the length of one side:"))
        print(" \nit's volume is" , ((3 * (3 ** 0.5))/2)* s ** 2 , "units cubed\n       ")
    else:
        print("    \nsorry, we can't do with more than 6 sides\n        ")


def isprime():
    ip = int(input("enter your number:"))
    f = 0
    for i in range(2, ip):
        if ip % i == 0:
            print("  \nThis is not a prime\n   ")
            f = 1
            break
    if f == 0:
        print(" \nThis is a prime\n   ")


def prop():
    ip = input("enter the first fraction numerator:")
    i = input("enter the first fraction's denominator:")
    it = input("enter the second fraction's denominator:")
    print("the numerator is equal to:",int(ip)/int(i)*int(it))


def log():
    ip = input("enter the number you want to geat the log of:")
    print(" \nthe log 10 of",ip," is:",math.log(int(ip)),"\n       ")


def cubevol():
    ip = input("enter the length of one side:")
    print(" \nthe cube's volume is equal to",int(ip)**3,"units cubed\n  ")


def isittriangle():
    b = 0
    ip = input("first side length:")
    b=int(ip)
    i = input("second side length:")
    if int(i)>int(ip):
        b=int(i)
    else:
        b=int(ip)
    it = input("third side length:")
    if int(it)>b:
        b=int(it)
    else:
        b=b
    if b==int(ip):
        if int(it)**2+int(i)**2==int(ip)**2:
            print(" \nit is a right angled triangle\n ")
        elif int(it)+int(i)==int(ip):
            print(" \nit is a triangle\n ")
        else:
            print(" \nit is not a triangle\n ")
    elif b==int(i):
        if int(ip)**2+int(it)**2==int(i)**2:
            print(" \nit is a right angled triangle\n ")
        elif int(ip)+int(it)>int(i):
            print(" \nit is a triangle\n ")
        else:
            print(" \nit is not a triangle\n ")
    else:
        if int(i)**2+int(ip)**2==int(it)**2:
            print(" \nit is a right angled triangle\n ")
        elif int(i)+int(ip)>int(it):
            print(" \nit is a triangle\n ")
        else:
            print(" \nit is not a triangle\n ")



def triarea():
    ip = input("enter base length:")
    i = input("enter height:")
    print("             \nthe area of this triangle is:",(int(ip)*int(i))/2,"units square\n               ")


def rectarea():
    ip = input("enter length")
    i = input("enter width:")
    print("          \nthis is the rectangle's area:",int(i) * int(ip),"units square\n                  ")


def spherevolume():
    ip = input("enter radius:")
    print("         \nthis sphere's volume is:",4/3 * math.pi * int(ip) ** 3,"units cube\n                ")


def circlearea():
    ip = input("enter radius:")
    print("     \nthis is the circle's area:",math.pi * int(ip) ** 2,"units\n                       ")



def circumference():
    ip = input("enter radius:")
    print("                  \nthis is the circle's circumference",2 * math.pi * float (ip),"units\n                  ")


def divideby():
    ip = input("enter number:")
    i = input("enter the second number:")
    if int(ip)==0:
        print("it is not possible to divide by 0")
    else:
        print("                    \nthe result is",int(ip)/int(i),"\n                    ")


def substractby():
    ip = input("enter a number:")
    i = input("enter the second number:")
    print("                  \nthe result is",int(ip)-int(i),"\n                     ")



def addby():
    ip = input("enter a number:")
    i = input("enter another number:")
    print("                      \nthe result is",int (ip) + int (i),"\n                          ")


def multiplyby():
    ip = input("Enter a number:")
    i = input("enter another number to multiply with the first number:")
    print("               the result of", int (ip),"*",int (i),"is equals to:",int (ip)*int (i),"\n                  ")


def gauss():
    ip = input("Enter a number:")
    print("                     \nthe sum of every number until",int(ip),"is",(int(ip)+1)*(int(ip)/2),"\n               ")





def factorial():
    ip = input("Enter a number:")
    print("     \nthis number's factorial",math.factorial(int(ip)),"\n              ")



def calculator():
    ip = int(input("1:gauss\n2:factorial\n3:multiply\n4:add\n5:substract\n6:divide\n7:proportionality\n8:circumference\n9:circle area\n10:sphere volume\n11:rectangle area\n12:triangle area\n13:is it a triangle?\n14:cube volume\n15:log 10\n16:is it prime?\n17:prism\n18:speed calculator\n19:at which height did your ball go\n20:a little math game\n21:chess\n22:exit\n23:LCM:"))
    if int(ip)==1:
        gauss()
    elif int(ip)==2:
        factorial()
    elif int(ip)==3:
        multiplyby()
    elif int(ip)==4:
        addby()
    elif int(ip)==5:
        substractby()
    elif int(ip)==6:
        divideby()
    elif int(ip)==7:
        prop()
    elif int(ip)==8:
        circumference()
    elif int(ip)==9:
        circlearea()
    elif int(ip)==10:
        spherevolume()
    elif int(ip)==11:
        rectarea()
    elif int(ip)==12:
        triarea()
    elif int(ip)==13:
        isittriangle()
    elif int(ip)==14:
        cubevol()
    elif int(ip)==15:
        log()
    elif int(ip)==16:
        isprime()
    elif ip == 17:
        prism()
    elif ip == 18:
        conv()
    elif ip == 19:
        ballheight()
    elif ip == 20:
        game()
    elif ip == 21:
        count()
    elif ip == 22:
        exit(0)
    elif ip == 23:
        lowest_common_multiple()
    else:
        print(" \nthis option is not in list\n      ")



while 1:
    calculator()
