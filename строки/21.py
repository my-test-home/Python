
""""" СЧИТАЕТ ПО ФОРМУЛЕ
import math
a=int(input())
b=int(input())
c=int(input())
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(s)

"""""

"""""
(−15,12]∪(14,17)∪[19,+∞) определить вохждения числа в диапозон
a=int(input())
if (a >-15  and a <=12 or a == 15 or a == 16 or a >= 19):
    print(True)
else:
    print(False)
"""""


"""""
import math

a=float(input())
c=float(input())
b=input()

if b == "+":
    f = a + c

elif b == "-":
    f = a - c

elif b == "/":
    if (b == "/" and c != 0):
        f = a / c
    else:
        f="Деление на 0!"

elif b == "*":
    f = a * c

elif b == "mod":
    if (b == "mood" and c != 0):
        f = (a / c) - (a // c)
    else:
        f="Деление на 0!"


elif b == "pow":
    f = a**c

elif b == "div":
    if (b == "div" and c != 0):
        f = int(a // c)
    else:
        f="Деление на 0!"
print(f)

"""""


"""""
companies = ["Microsoft", "Google", "Oracle", "Apple"]
i = 0
while i < len(companies):
    print(companies[i])
    i += 1
"""""

"""""
a=int(input())
b=int(input())
c=int(input())

d = [a,b,c]
d1 = max(d)
d2 = min(d)
print (max(d))
print (min(d))
for item in d:

    if (item != max(d) and item != min(d)) :
        print(item)
"""

"""
s=0
kol=0
a=int(input())
b=int(input())
if(b<a):
    s = a
    a = b
    b = s

for i in range(a,b+1):
   if (i%3 == 0):
      s=s+i
      kol=kol+1
print(s/kol)

"""

"""
# округляет print(7//3)

import math

a=float(input())
c=float(input())
b=input()

if b == "+":
    f = a + c

if b == "-":
    f = a - c

if b == "/":
    if (b == "/" and c != 0):
        f = a / c
    else:
        f="Деление на 0!"

if b == "*":
    f = a * c

if b == "mod":
    if (b == "mod" and c != 0):
        f = a % c
    else:
        f="Деление на 0!"


if b == "pow":
    f = a**c

if b == "div":
    if (b == "div" and c != 0):
        f = int(a // c)
    else:
        f="Деление на 0!"
print(f)
"""

"""
import math
a=input()
if a == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    rez = math.sqrt(p*(p - a)*(p - b)*(p - c))
if a == "прямоугольник":
    a = float(input())
    b = float(input())
    rez = a * b
if a == "круг":
    pi = 3.14
    r = float(input())
    rez = pi * (r ** 2)

print(rez)

"""

"""
i=0
b=[]
while ( i <=100 ):
   i = int(input())
   if(i>=10 and i<=100): b.append(i)

for i in b:
    print(i)
"""
"""
a = int(input())
if (a % 4 == 0 and a % 100 !=0) or a % 400 == 0:
    print("Високосный")
else:
    print("Обычный")
"""

"""
a = int(input())
b = int(input())
h = int(input())
if ( h >= a  and h <= b ):
    print('Это нормально')
if ( h > b ):
    print('Пересып')
if ( h < a ):
    print('Недосып')
"""
"""
a=int(input())
b=int(input())
c=int(input())

d = [a,b,c]
d1 = max(d)
d2 = min(d)
d.remove(d1)
d.remove(d2)

print (d1)
print (d2)
print (d[0])
"""

"""
a=str(input())

if(int(a[0])+int(a[1])+int(a[2]) == int(a[3])+int(a[4])+int(a[5])):
    print('Счастливый')
else:
    print('Обычный')
"""

"""
numb = input()
a, b = numb[:3], numb[-3:]

print(a)
"""
"""
a=str(input())

if(int(a[0])+int(a[1])+int(a[2]) == int(a[3])+int(a[4])+int(a[5])):
    print('Счастливый')
else:
    print('Обычный')
 """

"""
a=str(input())

def ov(a):

    if (int(a) >= 10):
        s = int(a[-1])

        b=int(a)-s
        b=str(b)
        s = int(b[-1])
        s1 = int(b[-2])
        s3 =(s1*10)+s
        if(s3==10):
            return True
        else:
            return False
    else:
        return False

def st(a):

    if (int(a[-1]) == 1 and ov(a) != True):

        return True
    else:
        return False

def ta(a):
    if (( int(a[-1]) == 2 or int(a[-1]) == 3 or int(a[-1]) == 4) and ov(a) != True):

        return True
    else:
        return False
def ov_fin(a):
    if(st(a) != True and ta(a)!= True):
        return True
    else:
        return False
#-----------------------------------------
if(ov_fin(a) == True):
    print(a+" программистов")

if(ta(a) == True):
    print(a+" программиста")

if(st(a) == True):
    print(a+" программист")


num = str(input())
ov = ('0', '11', '12', '13', '14', '5', '6', '7', '8', '9')
ta = ('2', '3', '4')
print(num.endswith(ov))

if num.endswith(ov):
    print(num + " программистов")
elif num.endswith('1'):
    print(num + " программист")
elif num.endswith(ta):
    print(num + " программиста")


n=int(input())
print(n,'программист'+('ов' if n%10==0 or 4<n%10<10 or 10<n%100<15 else 'а' if 1<n%10<5 else ''))

"""

"""
a = [1, 2, 3]
b = a
# значения списка b?
print(b)
print(a)
a[1] = 10
# значения списка b?
print(b)
print(a)
b[0] = 20
# значения списка a?
print(b)
print(a)
a = [5, 6]
# значения списка b?
print(b)
print(a)
"""

"""
A = input().split()
b=0
for i in range(len(A)):
   b =b+ int(A[i])
print(b)
"""
"""
a = [int(s) for s in input().split()]
c=[]
a.sort()

for elem in a:

    print(elem, end='')
    """
"""
A = [10, 10, 23, 10, 123, 66, 78, 123]
counter = {}

for elem in A:

    counter[elem] = counter.get(elem, 0) + 1

print(counter[elem])

doubles = {element: count for element, count in counter.items() if count > 1}

print(doubles)
"""
"""
def f(x):
    if(x<=-2):
        return (1-(x+2)**2)
    if(x>-2 and x<=2):
        return (-(x/2))
    if (x > 2):
        return ((x-2)**2+1)
print(f(1))
"""
"""
a = int(input())
x=0
y=0
for i in range(a):
    b = input().split()
    if(b[0]=='север'): y=y+int(b[1])

    if (b[0]=='запад'): x=x-int(b[1])

    if (b[0]=='юг'): y=y-int(b[1])

    if (b[0]=='восток'): x=x+int(b[1])
 # d = {'север': [0, 1], 'запад': [-1, 0], 'юг': [0, -1], 'восток': [1, 0]}
print(x,y)


# a//b  	Целочисленное деление - Деление в котором возвращается только целая часть результата. Часть после запятой отбрасывается.
# a%b остаток от делени
#print(minutes // 60, minutes % 60, sep = '\n')

# put your python code here

#slicing

ii=[]
b = input().split()

for i in range(len(b)):


    if(i==0):
        print(int(b[len(b)-1]) + int(b[i+1]))
        print("1-")
        ii.append(int(b[len(b)-1]) + int(b[i+1]))

    if(i == len(b)-1):
        print(int(b[len(b)-1]) + int(b[0]))
        print("2-")
        ii.append(int(b[len(b)-1]) + int(b[0]))
    if(i !=0 and i != len(b)-1):
        print(int(b[i-1]) + int(b[i+1]))
        print("3-")
        ii.append(int(b[i-1]) + int(b[i+1]))

#myString = ' '.join(ii)
#print(myString)

"""




















