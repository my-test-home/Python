f = open(r'C:\Python\text.txt','r')
#считывает весь текст
#text= f.read()

# strip() убирает в конце строки спец символы \n

text = f.readline().strip()


print(text)

with open(r'C:\Python\text.txt') as inf:
    for line in inf:
       line=line.strip()
       print(line)


#запись в фаил
out = open(r'C:\Python\text.txt','w')
out.write('jjjjj\n')
out.write(str(25))
out.close()

если проблема в юникоде
with open("file.txt", "r", encoding='utf-8') as file: