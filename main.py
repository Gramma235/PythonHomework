str = input('Введите строку, где одно слово является обращением другого: ')
count=0
for i in str:
    if i != ' ':
        count+=1
    else:
        word=str[:count]
        word=word[::-1]
        str=str[count+1:]
        count = 0
        str2 = str
        for i in str:
            if i != ' ':
                count += 1
            else:
                if str2.startswith(' '):
                    str2 = str2[1:]
                else:
                    str2 = str
                word2 = str2[:count]
                str2=str2[count:]
                count = 0
                if word==word2:
                    print(word[::-1],word2)
                    word=''
                    word2=''
                else:
                    word2=''
