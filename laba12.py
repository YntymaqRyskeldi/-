
# Файлдағы берілген орынға жол кірістіру
# 1. Жолды енгізіеміз
s = str(input('s = '))

# 2. Кірістіру орнын енгізіңіз (0-ден бастап нөмірленген).
#    Егер орын файлдағы жолдар санына тең болса,
#  содан кейін жол файлдың соңына қосылады.
pos = int(input('pos = '))

# 3. Оқу үшін мәтіндік файлды ашамыз
f = open('text_file.txt', 'r')

# 4.Файлдан L тізіміне дейінгі барлық жолдарды оқып аламыз
L = f.readlines()

# 5.  pos дұрыстығын тексереміз
if (pos<0) or (pos>len(L)):
    f.close()
    exit()

# 6. pos соңғы жолдан кейінгі жол екенін тексеру
if pos==len(L):
    # L тізімінің соңына жол қосу керек
    L[len(L)-1] += '\n'
    L2 = L + [s] # s жолын L тізімінің соңына қосамыз
else:
    # Құрамында жаңа L2 тізімін жасаймыз
    # L тізімі жаңа жол s pos позициясына енгізілген.
    L2 = []

    # Элементтерді L-ден L2-ге кірістіру орнына дейін көшіріңіз
    L2 = L2 + L[:pos] # использовать срез

    # L2 тізіміне s + жаңа жолды енгіземіз
    L2 = L2 + [s + '\n']

    #   pos дан кейін жататын элементтерді L-ден L2-ге көшіреміз
    L2 = L2 + L[pos:] # кесінді ретінде пайдаланамыз

# 7
f.close()

# ------------------------------------
# жаңадан жасалған L2 тізімін файлға жазыңыз
# 8. Жазу үшін файлды ашамыз
f = open('text_file.txt', 'w')

# 9.  L2 тізімді жазамыз
for line in L2:
    f.write(line)

# 10.
f.close()
'''

# Мәтіндік файлдағы жолды ауыстыру
# 1. Исходная строка
s = "Hello world!"

# 2. Көрсетілген позиция (0-ден бастап нөмірленген)
pos = 3

# 3. 
f = open('text_file.txt', 'r')

# 4. Файлдан L тізіміне дейінгі барлық жолдарды оқып аламыз
L = f.readlines()

# 5. Заменить строку в списке в позиции pos
if (pos >= 0) and (pos < len(L)):
    # в последней строке '\n' не добавлять
    if (pos==len(L)-1):
        L[pos] = s
    else:
        L[pos] = s + '\n'

# 6.
f.close()

# ------------------------------------
# Записать измененный список в файл
# 7. Открыть файл для записи
f = open('text_file.txt', 'w')

# 8. Записать список
for line in L:
    f.write(line)

# 9.
f.close()
'''