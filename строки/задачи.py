s = input()

b=s.upper()  #ATGCC делает все большими

#можно s = input().upper()
print(((b.count('G')+b.count('C'))/len(s))*100)

"""
считает по формуле 

"""


s = input()

b=s.upper()  #ATGCC делает все большими


print(((b.count('G')+b.count('C'))/len(s))*100)




#---------------------------------------------------------------------------
"""
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот 
символ и количество его повторений в этой позиции строки.

"""

s = input()

ii=1
b=''

for i in range(len(s)-1):

    if ( s[i] == s[i + 1]):

       ii=ii+1

    else:
       b = b + s[i] + str(ii)

       ii = 1

print( b + s[len(s)-1] + str(ii))

#    input    aasssaaddffg
#    autput   a2s3a2d2f2g1

