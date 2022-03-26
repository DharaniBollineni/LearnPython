tList1=[0,1,2,3,4,5,6,7,8,9,10,11,15,13,1513]
i=0
print("print list of elements using while loop")  
while i<len(tList1):
    print("Element in the index {} is {}".format(i,tList1[i]))
    i=i+1

print("print list of elements using for loop")  
for x in tList1:
    print(x)

# print only even numbers for the list
print("print only even numbers for the list")  
for x in tList1:
    if x%2==0:
        print(x)

# print only prime nubmer for the list
#A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.
#2, 3, 5, 7 etc. are prime numbers as they do not have any other factors. But 6 is not prime (it is composite) since, 2 x 3 = 6. 
print("print only prime nubmer form the list")
primeList=[]
for x in tList1:      
    count=0
    if x>1:
        for i in range(2,x):
            if x%i==0:
                count= count+1
                break
        if count==0:
                primeList=primeList+[x]

print("given list is ",tList1)
print("prime numbers in the list are:", primeList)

print()
        
# print prime numbers using for- else loop from the list
print("print prime numbers using for- else loop form the list")
primeList=[]
for x in tList1:      
    #count=0
    if x>1:
        for i in range(2,x):
            if x%i==0:
                #count= count+1
                break
       # if count==0:
        else:
                primeList=primeList+[x]

print("given list is ",tList1)
print("prime numbers in the list are:", primeList)


# print elements in +ve and -ve index
tList2=['A','B','C','D','E']
print("lenght of list is ",len(tList2))
print("Actul list is ", tList2)
print("Elements with +ve and -ve index is ")
for i in range(len(tList2)):
    print("{} +ve index and {} -ve index is {}".format(i,i-len(tList2),tList2[i]))

