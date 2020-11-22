print('Задача 1: плюсы и минусы')
str1=input("Введите строку, содержащую плюсы и минусы так, чтобы после некоторых знаков шли нули: ")
plusnumber=0
minusnumber=0
pluszero=0
minuszero=0
for i in range(len(str1)):
    if str1[i]=='+':
        plusnumber+=1
    if str1[i]=='-':
        minusnumber+=1
    if str1[i:i+2]=="+0":
        pluszero+=1
    if str1[i:i+2]=="-0":
        minuszero+=1
print("К-во плюсов в строке:", plusnumber)
print("К-во минусов в строке:", minusnumber)
print("К-во плюсов с нулем в строке:", pluszero)
print("к-во минусов с нулем в строке", minuszero)
print('''
''')
print('Задача 2: замена и добавление')
str2=input('Введите строку. которая может начинаться на abc: ')
if str2.startswith('abc')==True:
    str2=str2.replace('abc','www')
    print(str2)
else:
    print(str2,'zzz',sep='')
print('''
''')
print('Задача 3: самое длинное слово')
str3=input('Введите слова, разделенные одним или несколькими пробелами: ')
wordlength=0
thebiggestword=0
for i in range(len(str3)):
    wordlength+=1
    if str3[i]==' ':
        if wordlength>thebiggestword:
            thebiggestword=wordlength
            wordlength=0
        else:
            wordlength=0
print(thebiggestword-1)



