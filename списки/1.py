#делает копию списка

lst=[12,33,4,3]
b = lst[:]
lst.remove(12)
print(lst)
print(b)

>>>[33, 4, 3]
   [12, 33, 4, 3]


d={'C':14,'A':12,'T':9,'G':18}

for key in d:
    print(key,end='')
#
# >>> CATG
#
#
print("")
for key in d.keys():
    print(key,end='')
#
# >>> CATG
#
#
print("")
for value in d.values():
    print(value,end='')
#
# >>> 1412918
#
#
print("")
for key,value in d.items():
    print(key,value,end=';')
#
# >>> 1412918
#
#

story_count = {'а':12, 'у':14, 'б':10, 'к':23, 'm':13, 'e':16, 'я':3, 'в':6,'t':24 }

# Добавляем ключ "туфля" со значением "род обуви, закрывающей ногу не выше щиколотки"
story_count['туфля'] = 'род обуви, закрывающей ногу не выше щиколотки'
#денамически записываем словарь

"""
for i in range(1,5):
    story_count[i] = '87'
print(story_count())
"""

#Метод get() возвращает значение по указанному ключу.
print(story_count.get('ж'))

#Проверить есть ли в словаре подобное значение

if('сто1' in story_count):
    print("ключ есть")

l=list(story_count.keys())
l.sort()
print(l)
------------------------------------------------------------------------------------------
"""
with open(r'C:\1\text.txt') as inf:
   
    



    for line in inf:
        line=line.lower()
        line1=line1+ line.strip()+" "

l=line1.split(' ')
print(l)
b = [5, 10, 1]

s=sorted(l)

print(s)


s=my_string.lower()

print(my_string)

b=s.split(' ')
print(b)

ks=sorted(b)




"""

b1=[]
file = r'C:\1\text.txt'
b=open(file).read().split('\n')
for line in b:
    line=line.lower()
    b1=b1+line.split(' ')

story_count = {'а':12, 'у':14, 'б':10, 'к':49, 'm':13, 'e':49, 'я':3, 'в':6,'t':24 }


def keywithmaxval(d):
   
    v = list(d.values())
# подав {'а':12, 'у':14, 'б':10, 'к':49, 'm':13, 'e':49, 'я':3, 'в':6,'t':24 }
# [12, 14, 10, 49, 13, 49, 3, 6, 24]
    print(v)
    k = list(d.keys())
# подав {'а':12, 'у':14, 'б':10, 'к':49, 'm':13, 'e':49, 'я':3, 'в':6,'t':24 }
# получим ['а', 'у', 'б', 'к', 'm', 'e', 'я', 'в', 't']

    return k[v.index(max(v))]



print(b1)
b1=set(b1)
ks=sorted(b1)

print(keywithmaxval(story_count))









