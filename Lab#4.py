 
#Example1
'''
print("Введите имя, отчество и фамилию: ")
s=input()
n=s.find( " " )#find(str[, start [, end]): жолдағы ішкі жолдың индексін қайтарады. Ішкі жол табылмаса, -1 саны қайтарылады.
name = s[:n]#вырезать имя
s = s[n+1:]
n=s.find( " " )
name2 = s[:n]#вырезать отчество
s=s[n+1:] #осталась фамилия
s=s + " "+name[0]+"."+name2[0]+"."
print(s)'''

#Example2
'''text = input("enter a string to convert into ascii values:")
ascii_values = []
for i in text:
    ascii_values.append(ord(i))
print(ascii_values)
'''
#Example3
'''s= "0123456789"
s1 = s[:3] + s[9:] #delete
s2 =s[:3] + "ABC" + s[3:]#insert
print(s1)
print(s2)'''

#Example4
'''
name = "MonicaGeller"
if name.isalpha() == True:#isalpha(): егер жол тек алфавиттік таңбалардан тұрса, True мәнін қайтарады
    print("All characters are alphabets")
else:
    print("All characters are not alphabets.")'''

#Example5
'''
string = "geeks-for-geeks"
print(string, "converted using title():", string.title())
#title(): Жолдағы барлық сөздердің бастапқы таңбаларын бас әріпке түрлендіреді'''


#Example6
'''
sentence = "i love PYTHON"

# бірінші таңбаны бас әріпке, ал басқаларын кіші әріпке түрлендіреді
capitalized_string = sentence.capitalize()

print(capitalized_string)'''

#Example7

'''text = 'Я люблю программировать на Python'
print(text.find('люблю',0,9)) #  find(str[, start [, end]): жолдағы ішкі жолдың индексін қайтарады. Ішкі жол табылмаса, -1 саны қайтарылады.'''

#Example8
'''text = 'He is {} year student of Satbayev University'
print(text.format(4))#format() функциясы жолдарды пішімдеу үшін пайдаланылатын кірістірілген String функциясы болып табылады.
print(list(text))#әртүрлі элементтердің жиынын немесе тізбегін сақтауға арналған деректер түрі.'''

#example9
'''a_str=' " a b " c d " '
replaced_str= a_str.replace(' " ' , " ")#жолдағы бір ішкі жолды екіншісімен ауыстырады
print(replaced_str)'''

#example10
s = 'WelCome to PyThon'
print(s.capitalize())#бірінші әріпті бас әріпке, қалғанын кіші әріпке түрлендіреді.
print(s.lower()) #барлық алфавиттік таңбаларды кіші әріпке түрлендіреді
print(s.swapcase()) # алфавиттік таңбалардың регистрін өзгертеді
print(s.title()) # барлық сөздердің бірінші әріптерін бас әріпке түрлендіреді
print(s.upper()) # барлық алфавиттік таңбаларды бас әріпке түрлендіреді

 

 #1.Кіші және бас әріптерді қамтитын жол енгізіледі. Бір жағдайда бірдей жолды шығару қажет, ол қай әріптердің үлкенірек екеніне байланысты. Егер тең болса, кіші әріпке түрлендіріңіз. 
'''
string = str(input())
upp = 0
low = 0
for i in string:
    if i.isupper():#isupper(): Жолдағы барлық таңбалар бас әріптер болса, True мәнін қайтарады.
        upp += 1
    else:
        low += 1
if upp > low:
    print(string.upper())#upper(): жолды бас әріпке түрлендіреді
else:
    print(string.lower())#lower(): жолды кіші әріпке түрлендіреді
    '''

#2.isdigit() жол әдісі жолда тек сандар бар-жоғын тексереді. Енгізуден екі бүтін санды сұрайтын және олардың қосындысын басып шығаратын программа жазыңыз.
'''a = input()
b = input()
while not(a.isdigit() and b.isdigit()):#isdigit(): егер жолдағы барлық таңбалар цифр болса, True мәнін қайтарады
    a, b = input(), input()
print(int(a) + int(b))'''

'''a = input()

while not (a.isdigit()):

   a = input()  

b = input()

while not (b.isdigit()):

   b = input()  

print(int(a)+int(b))  '''

 

   
