'''1.Тізімдерді, кортеждерді, жиындарды және сөздіктерді бір бағдарламаның ішінде көрсететін бағдарлама жаз.
Мәлеметтер ретінде әр студент өзіне байланысты ақпарат немесе резюмесін ұсыну қажет.
'''

'''2. Тізімдердегі, кортеждердегі, жиындардағы және сөздіктердегі әдістерді қарастырып,
барлығына ортақ 5 әдісті және ерекшеленетін бірнеше (2-3) әдістерді қолдананатын бағдарлама жаз.
'''

'''#LIST-------------------
print("\n", "List")
resume = ["Ryskeldi", "Yntymak", "20","87475687685", "Montaieva2", "Satbayev university", "Computer scince"]
print("name:", resume[0], "\nlasname:", resume[1], "\nage:",resume[2], "\nPhone number:", resume[3],
      "\naddress:",resume[4],"\neducation:", resume[5], "\nSpeciality:", resume[6])
 
resume.insert(3, "87769875211")#i-ші элементке x мәнін кірістіреді
print("\n", resume)

resume_list = ["yntymakryskeldi@gmail.com", "23.09.2002", "нет опыта"]
resume.extend(resume_list)#L тізімінің барлық элементтерін соңына қосу арқылы list тізімін кеңейтеді
print("\n", resume)

resume.copy()# тізімнің көшірмесін жасайды
print("\n", resume)

#resume.remove(4)#x мәні бар тізімдегі бірінші элементті жояды. Мұндай элемент болмаса ValueError
#print("\n", resume)

resume.pop(3)#i-ші элементті алып тастап, оны қайтарады. Егер индекс көрсетілмесе, соңғы элемент жойылады
print("\n", resume)

resume.reverse()#Тізімді кері ауыстырады
print("\n", resume)

resume.count(2)#x мәні бар элементтердің санын қайтарады
print("\n", resume)

resume.clear()#Тізімді тазартады
print("\n", resume)

#КОРТЕЖ---------------------------
print("\n", "Tuple")
tuple = ("Ryskeldi", "Yntymak","87475687685", "Montaieva2", "Satbayev university", "Computer scince")

k = tuple.count("Ryskeldi")
print("\n", k)

tuple2 = ("yntymakryskeldi@gmail.com", "23.09.2002", "нет опыта")

Tuple=tuple+tuple2

print(Tuple)
print('\nКоличество -', len(Tuple))
 
del tuple



#Жиын----------------------
set = {"Satbayev University", "Software Engineering", "Computer Science"}
print("\n", "Жиын")
print("\n", set)

set.add("course: 4")
print("\n", set)

set.remove("Software Engineering")
print("\n", set)

print("\n", len(set))

set2= {"Satbayev University", "cybersecurity", "Information Security System"}

print("\n", set2)
print("\n", set.difference(set2))

set.clear()
print("\n", set)

#Словарь----------------------------------
dict = {"IIN": "020923500544", "Phone number": "87475687685"}
print("\n", "Словарь","\n", dict)

dict["Phone number2"] = "87769875211"
print("\n", dict)

dict.pop("IIN")
print("\n", dict)

dict.copy()
print("\n", dict)

s = dict.get("Phone number")#возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
print("\n", s)

k = dict.keys()#возвращает ключи в словаре.
print("\n", k)
 
 '''
'''5. 5. Синонимдік сөздік
Сізге жұп сөздерден тұратын сөздік беріледі. Әрбір сөз оның жұптас сөзінің синонимі болып табылады. Сөздіктегі барлық сөздер әртүрлі. Берілген бір сөздің синонимін анықтаңыз.
Деректерді енгізу
Бағдарлама кіріс ретінде NN синонимдер жұбының санын алады. Бұдан кейін NN жолдары келеді, әр жолда дәл екі синоним бар. Осыдан кейін бір сөз келеді.
Шығару
Бағдарлама берілген сөздің синонимін шығаруы керек.
Ескерту
Бұл мәселені сөздіктерсіз шешуге болады (барлық енгізілген деректерді тізімде сақтай отырып), бірақ сөздік көмегімен шешу оңайырақ болады.
Примеры
входные данные
3
Hello Hi
Bye Goodbye
List Array
Goodbye
выходные данные
Bye
'''
'''
dict = {}
n = int(input())
for i in range(n):
    first, second = input().split()
    dict[first] = second
    dict[second] = first
print(dict[input()])'''


'''4. Рұқсат құқығы
Вирус бір суперкомпьютердің файлдық жүйесіне еніп, файлдарға қол жеткізу құқықтарын басқаруды бұзды. Әрбір NiNi файлы үшін онымен қандай әрекеттерге қол жеткізуге болатыны белгілі:
• запись W,
• чтение R,
• запуск X.

Файлға қатынасу құқықтарын бақылауды қалпына келтіру қажет (файлда жарамды операция орындалса, бағдарламаңыз әрбір сұрау үшін OK қайтаруы керек немесе операция жарамсыз болса, Access қабылданбады.
Деректерді енгізу
Кіріс файлының бірінші жолында NN (1≤N≤100001≤N≤10000) саны — берілген файлдық жүйеде қамтылған файлдар саны бар.
Келесі NN жолдарында файлдардың аттары және олармен рұқсат етілген операциялар бос орындармен бөлінген. Файл атауының ұзындығы 15 таңбадан аспайды.
Әрі қарай, MM саны (1≤M≤500001≤M≤50000) көрсетіледі - файл сұрауларының саны.
Соңғы MM жолдарында Operation File пішімінің сұрауы бар. Бір файлға сұраулардың кез келген санын қолдануға болады.
Шығару
MM сұрауларының әрқайсысы үшін Access denied немесе OK басып бөлек жолда басып шығарыңыз.
Примеры
входные данные
4
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
5
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog
выходные данные
OK
Access denied
Access denied
OK
OK

'''
n = int(input())  #қанша жол екенін береміз
x = {'write':'W','read':'R','execute':'X'}#Жиын
dict={}
for i in range(n):
    a,*b=input().split()#split() функциясы жолды жолдар тізіміне бөлу үшін пайдаланылады.
 
    dict[a]=set(b)
for i in range(int(input())):
    a,b=input().split()
    if x[a] in dict[b]:
        print('OK')
    else:
        print('Access denied')'''


