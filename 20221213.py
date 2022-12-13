import random
"""
list=[]

for i in range(10):
    list.append(random.randint(1,100))
print(list)


osszeg=0
db=0
for i in list:
    if i<50:
        osszeg+=i
        db+=1
print(f"A lista elemeinek összege: {osszeg}, darab {db}")
print(sum([x for x in list if x>50]))
print(len([x for x in list if x>50]))

n=len(list)
i=0
while i < n and list[i]!=50:
    i=i+1
print(f"Helye: {i}")
print("Van benne 50-es ha" if i<n else "Nincs benne")

#Szétválasztás
list=[]
paros=[]
paratlan=[]
for i in range(10):
    list.append(random.randint(1,10))
    if i%2==0:
        paros.append(i)
    else:
        paratlan.append(i)
print(paros)
print(paratlan)
"""

#Maximum és minimum kiválasztása
max=list[0]
min=list[0]
maxi=0
mini=0
for i in range(len(list)):
    if list[i]>max:
        max=list[i]
        maxi=i
    for i in range(len(list)):
    elif list[i]>min:
        min=list[i]
        mini=i
print(f"legnagyobb eleme: {max}, helye:{maxi}")
print(f"legnagyobb eleme: {min}, helye:{mini}")

for i in range(0,len(list)-1):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            csere=list[i]
            list[i]=list[j]
            list[j]=csere

