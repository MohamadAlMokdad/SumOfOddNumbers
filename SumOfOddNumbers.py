x=int(input("Enter a Number:"))

Sum=0
for i in range(1,x+1):
    if i % 2 != 0:
        Sum+=i

print(Sum)