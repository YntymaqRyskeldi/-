file = open('smth.txt', 'w')

while True:
    i = input("Введите элемент: ")
    if i ==" " or i =="":
        break
    file.writelines(str(i) + '\n')
file.close()

lst = []
file1 = open('smth.txt', 'r')

while True:
    line = file1.readline()
    if not line:
        break
    lst.append(int(line.strip()))
print(lst)

par = []
for i in lst:
    par.append(round(pow(abs(i),2)))
print(par)

print("Разница между первым и вторым списком",sum(par)-sum(lst))
print(sorted(lst))

print("min:", min(lst))
print("max:", max(lst))
print(bin(lst[1]))
print(hex(lst[1]))
print(oct(lst[1]))

print(list(enumerate(lst,1)))
print(max(list(enumerate(lst))))

file1.close()
