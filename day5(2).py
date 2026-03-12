#For Loop in Python

#example:01
name="Alishba"
for i in name:
    print(i)
    if(i=="b"):
        print("This is something special")

#example:02

colors=["Red","Blue","Green","Purple","Black"]
for i in colors:
    print("The color name is:" , i)
    for x in i:
        print(x)


#Range
for k in range(5):
    print(k+1)

for r in range(1,9):
    print(r)

for k in range(1,20,3):
    print(k)
 
