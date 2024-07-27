n1 = int(input("digite o n1: "))
n2 = int(input("digite o n2: "))
n3 = int(input("digite o n3: "))
if n1 > n2 or n1 > n3:
    print ("n1 é maior")
elif n2 > n1 and n2 > n3:
    print("n2 é maior")
elif n3 > n1 and n3 > n2:
    print ("n3 é maior")
elif n1 == n2 and n1 == n3 and n2 == n3:
    print ("equivalentes")