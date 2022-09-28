#EXAMPLE
#1
'''import random
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
index = random.randrange(0, len(x))
x[index]'''

#2
 '''import random

def randomnumber(N):
	minimum = pow(10, N-1)
	maximum = pow(10, N) - 1
	return random.randint(minimum, maximum)

print(randomnumber(10))
'''
#3
#randInt()-ке мысал.randint() — Python3 жүйесіндегі кездейсоқ модульдің кірістірілген функциясы. Кездейсоқ модуль әртүрлі пайдалы функцияларға қол
#жеткізуге мүмкіндік береді және олардың бірі кездейсоқ сандарды жасай алады
import random #Библиотеканы импорттап аламыз
r1 = random.randint(0, 100) #0 мен 100 аралығындағы кез келген санды генерациялайды
print("0 мен 100 аралығындағы рандомный сан -  % s" % (r1)) #Экранға шығарады


#4
import random
 

r1 = random.randint(0, 10)
print("0 мен 10 арасындағы кездейсоқ сан % s" % (r1))
 
 
r2 = random.randint(-10, -1)
print("-10 мен -1 арасындағы кездейсоқ сан % d" % (r2))
 
 
r3 = random.randint(-5, 5)
print("-5 пен 5 арасындағы кездейсоқ сан % d" % (r3))
