#делает копию списка

lst=[12,33,4,3]
b = lst[:]
lst.remove(12)
print(lst)
print(b)

>>>[33, 4, 3]
   [12, 33, 4, 3]


