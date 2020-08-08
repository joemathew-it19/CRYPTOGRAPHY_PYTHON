num=[]

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    num.append(value)

loc = int(input("enter location you want to enter"))
number = int(input("enter number to insert"))
num.insert(loc, number)

print('Updated List: ', num)
