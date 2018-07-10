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



