#Math, random, datetime, Canvas модульдерін қолданып әр модульден 5  функцияны қолданып бағдарлама жазу.
'''
import math
#1
def circle_area(r):
    return math.pi*r**2

print("Radius: ")

radius = int(input())
print("Area =", circle_area(radius))

#2
a = int(input())
b = int(input())
c = int(input())
p=a+b+c
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
x= round(S,4)  #round функциясы жуықтауға арналған 4-үтірден кейін 4 санға дейін жуықтайды
print("Периметр:",p)
print('Площадь:',x)

#3

print("{}! = {}".format(p, math.factorial(p)))

#4
gcd = math.gcd(radius, p)
print("GCD: ",gcd)
#5
print("Периметр log10: ",math.log10(p))

#-------------------------------
'''
'''
import random
#random 1
print('Случайное целое число:', end=' ')
print(random.randrange(0, 10, 2))   # только чётные числа

#2
example = list('abracadabra')
print(example)

print(random.sample(example, 5))
 #3
print(random.choice(list('abracadabra')))#choice бір кездейсоқ элементін қайтарады.

#4
seq = ["Cappuccino", "Latte", "Espresso", "Americano"]
random.shuffle(seq)
print(seq)
 #5
print(random.uniform(5.5, 25.5))#осы аралықтағы  кездейсоқ float сан
'''

#------------------------------
'''
#datatime
import calendar
calendar.TextCalendar().prmonth(2022,11)

import datetime
from datetime import date
from datetime import timedelta

dt_now = datetime.datetime.now()
print(dt_now)


current_date = date.today()
print(current_date)

current_date_time = datetime.datetime.now()
current_time = current_date_time.time()
print(current_time)

second = datetime.date(2023, 1, 1)
answer = second - datetime.date.today()
print("Жаңа жылға дейін: ", answer)

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("total seconds =", t.total_seconds())
'''

#----------------------------
#Canvas
'''
from tkinter import *

root = Tk()

frame = Frame(root, width=300, height=300)
frame.pack(expand=True, fill=BOTH)

canvas = Canvas(frame, bg='white', width=300, height=300)

coordinates = 20, 50, 210, 230
arc = canvas.create_arc(coordinates, start=0, extent=250, fill="green")
arc = canvas.create_arc(coordinates, start=250, extent=50, fill="red")
arc = canvas.create_arc(coordinates, start=300, extent=60, fill="yellow")
arc = canvas.create_arc(coordinates, start=400, extent=60, fill="blue")
canvas.pack(expand=True, fill=BOTH)

root.mainloop()


#------------------------------

'''
from tkinter import *


ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x300')
ws.config(bg='#345')

canvas = Canvas(
    ws,
    height=200,
    width=400,
    bg="#fff"
    )

canvas.pack()

canvas.create_text(
    200,100,
    fill="darkblue",
    font="Times 20 italic bold",
    text="Hello \nworld!!!")

ws.mainloop()



#Canvas модулін (оның ішінде Tkinter) қолданып, әр студент өз атын өрнектеп  логотип жасап келсін

from tkinter import *
import math

root = Tk()
root.title('Логотип')
root.resizable(width=False, height=False)

canvas = Canvas(width=800, height= 1000, bg='white')
canvas.pack()

canvas.create_text(
    405,400,
    fill="black",
    font="Times 80 ",
    text="Ryskeldi")


r = 50
n = 16

for k in range(n):
    if n % 2 == 0:
        k1 = (k + n / 2 - 1) % n
    else:
        k1 = (k + (n - 1) / 2) % n

    p1 = (400 + r * math.cos(2 * 3.14 * k / n), 300 + r * math.sin(2 * 3.14 * k / n))
    p2 = (400 + r * math.cos(2 * 3.14 * k1 / n), 300 + r * math.sin(2 * 3.14 * k1 / n))
    canvas.create_line(p1, p2, fill ='black',width=3)

canvas.create_oval(600,600,210,210,outline="black", width=6)
root.mainloop()

