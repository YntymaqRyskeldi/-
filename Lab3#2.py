'''А және В екі бүтін сандар берілген. А<B болса, өсу ретімен н/е
басқаша жағдайда кему ретімен А-дан В-ға дейінгі барлық сандарды басып шығарыңыз
'''
A = int(input("A = "))
B = int(input("B = "))

if(A<B):
    for i in range(A, B+1):
        print(i)
elif A>B:
    for i in range (A-B):
        print(A-i)
else:
    print("A==B")
