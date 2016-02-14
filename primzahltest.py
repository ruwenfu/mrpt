#import math as m
#import numpy as np
import string
import sys

firstprimes=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,\
            83,89,97,103,107,109,113,127,131,137,139,149,151,157,163,167,173,\
            179,181,191,193,197,199)

def calc_d_j(n1):
    stop=False
    d=0
    j=0
    while not stop:
        if n1%2==0:
            j+=1
            n1//=2
        else:
            d=n1
            stop=True
    return [d,j]
    
def t1(a,d,j,n):
    if mod_exp(a,d,n)==1:
        return True
    else:
        return False

def t2(a,d,j,n):
    r=False
    for i in range(j):
        b = d * (2**i)
        if mod_exp(a,b,n)==n-1:
            r=True
            break
    return r
        
def mod_exp(a,b,n):
    number = 1
    while b:
        if b & 1:
            number = number * a % n
        b >>= 1
        a = a * a % n
    return number
#############################################################################
######   Miller-Rabin-Primzahltest (MRP)#####################################
#############################################################################
def MRP(n, anzahl=25):
    prim=True
    if n in firstprimes:
        return True
        
    n1=n-1
    DJ=calc_d_j(n1)
    d=DJ[0]
    j=DJ[1]
    for i in range(anzahl):
        a=firstprimes[i]
        if t1(a,d,j,n)==False:
            if t2(a,d,j,n)==False:
                prim=False
                break

    #if prim==True:
    #    print(n,"ist eine primzahl, wahrscheinlichkeit:",">",(1-((1/4)**anzahl)))
    #else:
    #    print(n,"ist KEINE primzahl")
    return prim        

def MRP_print(n):
    if MRP(n)==True:
        print(n,"ist eine primzahl")
    else:
        print(n,"ist KEINE primzahl")

def nextprime(n,M=10000):
    n+=1
    if M>n:
        M=n-1
    prim=False
    MPrimes=[]
    
    if n%2==0:
        n+=1

    def checkM(n):
        for i in range(len(MPrimes)):
            if n%MPrimes[i]==0:
                return True
        return False

    for i in range(2,M):
        if MRP(i)==True:
            MPrimes.append(i)
        i+=1
        
    while not prim:
        if checkM(n)==False:
            if MRP(n,10)==True:
                prim=True
            else:
                n+=2
        else:
                n+=2
    print("")
    print("die nächste primzahl ist")
    print(n)
    #return n

def isexpression(s):
    for c in s:
        if not c in string.digits and not c in ('*', '+', '-', '/', 'e'):
            return False
    return True

def check_and_execute(s, func):
    if s.isdigit():
        #print("Modus: Zahlen")
        func(int(s))
    elif isexpression(s):
        #print("Modus: Ausdruck")
        func(int(eval(s)))
    else:
        print("Fehler")


if len(sys.argv)<=1:
    sys.exit(1)
else:
    if sys.argv[1]=='nextprime':
        #print("nextprime")
        check_and_execute(sys.argv[2], nextprime)
    elif sys.argv[1]=='isprime':
       # print("primzahltest")
        check_and_execute(sys.argv[2], MRP_print)
    else:
        print(sys.argv[1],"nicht bekannt")



"""
(19:46:02) Gorath: def nextprime(n,M=10000):

        n+=1

            if M>n:

                    M=n-1

                        prim=False
                        (19:46:29) Gorath: da hab ich überlegt obs sorum günstiger wäre 

                        def nextprime(n,M=10000):

                            if M>=n:

                                    M=n

                                           n+=1

                                               prim=False


"""
