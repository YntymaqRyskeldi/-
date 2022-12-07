
#Лабараториялық жұмыс №12 Файлмен жұмыс жасауды үйрену. Минимум 5 операция жасайтын ауқымды бағдарлама құру.

import os

file = open("text.txt", "r")

content = file.read(6)
print(content)

more_content = file.read(12)
print(more_content)

file.close()


with open("python.txt", "w") as file:
    file.write("Python is awesome\n")
    file.write("I love Python")



with open("python.txt", "a") as file:
    file.write("\nPython is my favorite programming language")


with open("python.txt", "r") as file:
    lines = file.readlines()
    print(lines)


with open("java.txt", "w") as file:
   lines = ["Java is also awesome", "\nJava is my second favorite programming language"]
   file.writelines(lines)

os.rename("text.txt","message.txt")