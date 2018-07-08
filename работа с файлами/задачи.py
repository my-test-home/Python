
"""
 Sample Input:

считать с файла строку
a3b4c2e10b1

и сохранить в фаил
Sample Output:

aaabbbbcceeeeeeeeeeb



"""

f = open(r'C:\Python\text.txt','r')

text = f.readline().strip()

def coding(s):
    t=""
    flag= True
    simvol=""
    sifra=0
    for i in range(len(s)):

        if(s[i].isalpha()):
            if (flag == False):
                flag=True
                for l in range(sifra):
                    t=t+str(simvol)

                sifra = 0
            simvol = s[i]
        else:
            if(flag == True):
                flag=False
                sifra = sifra + int(s[i])
            else:
                sifra = (sifra*10)+int(s[i])

    for l in range(sifra):
        t = t + str(simvol)
    return t


out = open(r'C:\Python\text.txt','w')
out.write(coding(text))
out.close()


"""
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам:

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом: 
 Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667


"""

out = open(r'C:\Python\text1.txt','w')

ch=0
ln1=0
ln2=0
ln3=0

with open(r'C:\Python\text.txt', "r", encoding='utf-8') as inf:
    for line in inf:

       line=line.strip().split(';')
       s=round(((int(line[1])+int(line[2])+int(line[3]))/3),9)
       ln1=ln1 +int(line[1])
       ln2=ln2 +int(line[2])
       ln3=ln3 +int(line[3])
       ch =ch+1
       out.write(str(s)+"\n")
l1=round((ln1/ch),9)
l2=round((ln2/ch),9)
l3=round((ln3/ch),9)
out.write(str(l1)+" "+str(l2)+" "+str(l3))


"""

lst='Петров;85;92;78'
b=lst.split(';')

print(b)

a=float(58+72+85)/3





