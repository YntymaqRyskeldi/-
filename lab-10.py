#10 кірістірілген функцияны алып, бір бірімен үйлестіріп бағдарлама жазамыз. Функциялар осыған дейін біз
# қолданбаған болуы қажет.

#бир функция орындалып сол файлдын ишине салынып турса деп ойластырдым
#не туралы жасауға болатынын қарастырып көріндерші, мен оларды файлдарга салып отырумен айналысамын деп
#2 кірістірілген функциядан алып бирдене жасаса тема болады

sometext = 'Salem'
file = open('smth.txt', 'w')
file.write(str(sometext))
file.close()

file = open('text.txt', 'r')
text = file.read()
print(text)
file.close()

file = open('text.txt', 'r')
line = file.readline()
print('\n', line)
file.close()

file = open('text.txt', 'r')
word = file.read(6)
print('\n', word)
file.close()


'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Student's name is " + name + " and age is " + str(age))

    def performance(self, grades):
        self.grades = grades
        print("The grade of student is: " + grades)


class Girl(Student):
    def __init__(self, name, age):
        super().__init__(name, age)
        print("Girl class is ready")

    def whichclass(self):
        print("This is Girls class which is a child class of Student class.")


stu1 = Student("John", 16)
stu1.performance("A+")
stu2 = Student("Smith", 24)
stu2.performance("B")
print("\n")
girl1 = Girl("Anna", 21)
girl1.whichclass()
girl1.performance("B")
'''