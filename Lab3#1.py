"""
Екі бүтін А және В саны берілген (А ≤ B бар). А-дан В-ға дейінгі барлық сандарды басып шығарыңыз.
"""
A = int(input("A = "))
B = int(input("B = "))

if(A<=B):
    for i in range(A, B+1):
        print(i)
else:
    print("A>B")
