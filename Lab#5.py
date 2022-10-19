'''Тізімде қолданылатын функциядарды қолданып, программа жазып шығу.
Тізім ретінде әр студент өзінің резюмесін ұсынсын. Және сол тізіммен жұмыс жасасын.
'''
 
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
'''.1) Бағдарламалау секцияларына қатысатын әртүрлі топтағы студенттерді
таныстыруды сұрайтын бағдарламаны жазыңыз.Тізімді сыныптардың өсу реті бойынша сұрыптау қажет.
Фамилиялар мен сыныптардың тізімін басып шығарыңыз
'''
'''
class Student:
    def __init__(stud, full_name="", group_number="", student_progress=[]):
        stud.full_name = full_name
        stud.group_number = group_number
        stud.student_progress = student_progress
    def __repr__(stud):
        return repr(("Студент: " + stud.full_name + "  Группа: " + stud.group_number))
    def addStudent(stud):
        print("Введите Фио: ")
        stud.full_name = input()
        print("Введите номер группы: ")
        stud.group_number = input()
        print("Введите последние 3 оценок : ")
        stud.student_progress = []
        for i in range(3):
            score = int(input())
            stud.student_progress.append(score)
    def getMarks(stud): # бағалар тізімін қайтарады
        return stud.student_progress
st_size = 5
sz_ocenki = 3
student_list = [] # студенттер тізімі
for i in range(st_size):
    st = Student()
    st.addStudent()
    student_list.append(st);
for student in student_list:
    print(student.getMarks())
    print(student.__repr__())'''

'''.2) Тізім қайтаратын функция жазып шығу.
Алдын ала студенттердің пәндері және бағалары бар тізім құрастыр.
Және сол тізім бойынша студенттің атын еңгізген кезде,
сол студенттің бағаларын шығарып бертін болсын.
'''
'''
student_grades = [
  {"name": "Bob","grades": [4, 3, 5, 5, 4]},
  {"name": "Alice","grades": [3, 2, 3, 4, 3]},
  {"name": "Aliya","grades": [3, 5, 4, 3, 5]},
  {"name": "Madi","grades": [5, 5, 5, 4, 5]},
  {"name": "Alihan","grades": [5, 4, 5, 4, 4]}]

def get_student_grades(students):
  string = str(input('Name student: '))
  for student in students:
      if student["name"] == string:
          print(student["grades"])
    

get_student_grades(student_grades)
'''
'''3). Пайдаланушыға бүтін мәндерді сұрайтын және оларды тізім ретінде сақтайтын
бағдарламаны жазыңыз. Мәндерді енгізудің аяқталуының көрсеткіші ретінде нөлді
пайдалану керек. Содан кейін бағдарлама пайдаланушы енгізген барлық сандарды
(нөлден басқа) өсу ретімен көрсетуі керек - әр жолға бір мән.
Сұрыптау үшін sort әдісін немесе sorted функцияны пайдаланыңыз.
'''
'''
list = []
while (number := input('Enter number: ')) != '0':
  try:
    list.append(int(number))#ерекше жағдайды шығара алатын операция блоктың ішіне орналастырылады try.
         #Ал қате орын алған кезде орындалуы керек код ішінде болады except. дизайны else тармағы бар шартты мәлімдемеге ұқсас.
  except ValueError:
   ...
list.sort()
print("Сандардың өсу ретімен тізімі: ")
for i in list:
    print(i)
    '''
