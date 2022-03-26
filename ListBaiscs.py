# list creation / basics of list
# List Datat type is collection of Objects of any type

print("**************************************************************************************************************************************************************")
#Basic list creation
print("**************************************************************************************************************************************************************")

#Empty list creation
print("Empty list creation")
emtList=[]                      #create empty list
print("Empty list : ",emtList)   #[]
print(type(emtList))                   #variable type --> <class 'list'>

print("**************************************************************************************************************************************************************")

# create list with existing similar elements
print("create list with existing similar elements")
existEltsList=[10,20,30,40]
print("list Elements : ",existEltsList)#[10,20,30,40]
print(type(existEltsList))                   #variable type --> <class 'list'>

print("**************************************************************************************************************************************************************")

# create list with existing different elements
print("create list with existing different elements")
exL=[10,'e','@','rani']
print("list Elements : ",exL)#[10,'e','@','rani']
print(type(exL))                   #variable type --> <class 'list'>
l1=len(exL)

#individual list elements type details
print("individual list elements type")
i=0
while i<l1:
    print(type(exL[i]))
    i=i+1
#print(type(exL[0]))                   #<class 'int'>
#print(type(exL[1]))                    #<class 'str'>
#print(type(exL[2]))                    #<class 'str'>

print("**************************************************************************************************************************************************************")

#Create list by dynamic input
print("Create list by dynamic input")
dl= input("Enter a list")       #Enter a list[10,20,40]
print("Elements",dl)            #'[10,20,40]'
print(type(dl))                       #<class 'str'>


print("**************************************************************************************************************************************************************")

#Note: we cannot enter a list directly where python considers it as a sting.
#To overcome this use eval() method as below and find difference.


#Create list using dynamic input
print("Create list input dynamic using :")
dl= eval(input("Enter a list")) #Enter a list['10','e','$','ani','ani123@','10''20']
print("Elements ",dl)           #Elements ['10', 'e', '$', 'ani', 'ani123@','1020']
print(type(dl))                        #<class 'list'>
l2=len(dl)
print("List of elements in dl list and its type")
j=0
while j<l2:
    print(" dl[0] is {} and its type is            {} ".format(dl[j],type(dl[j])))
    j=j+1
#print(" dl[0] is {} and its type is       {} ".format(dl[0],type(dl[0])))
#print(" dl[1] is {} and its type is       {} ".format(dl[1],type(dl[1])))
#print(" dl[2] is {} and its type is       {} ".format(dl[2],type(dl[2])))
#print(" dl[3] is {} and its type is       {} ".format(dl[3],type(dl[3])))
#print(" dl[4] is {} and its type is       {} ".format(dl[4],type(dl[4])))

print("**************************************************************************************************************************************************************")

#with list() we can convert the sequence to lsit
print("with list() we can convert the sequence to list")
lFun=list(range(0,10))
print("list elements",lFun)                 #list elements [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(lFun))                           #<class 'list'>

lFun=list(range(0,10,2))
print("list elements",lFun)                 #list elements [0, 2, 4, 5, 6, 8]
print(type(lFun))                           #<class 'list'>

print("**************************************************************************************************************************************************************")

# convert string to list
print("convert string to list")
str1='Alis and bob'
sToList=list(str1)
print("Converted string "+str1+" to list ",sToList)         #Converted string Alis and bob to list  ['A', 'l', 'i', 's', ' ', 'a', 'n', 'd', ' ', 'b', 'o', 'b']
print(type(str1))                    #<class 'string'>
print(type(sToList))                 #<class 'list'>

print("**************************************************************************************************************************************************************")

#list to list
print("list to list")
s=[10,20]
ss=list(s)
print(ss)                     #[10, 20]
print(type(s))               #<class 'list'>
print(type(ss))               #<class 'list'>

print("**************************************************************************************************************************************************************")

#convert a string to list using split(), split can be done using a space or any symbol, defult spliting is done by space, where return type of split() is list
print("convert a string to list using split(), split can be done using a space or any symbol, defult spliting is done by space, where return type of split() is list")
strSp=input("Enter a sting")                 #Enter a sting Alise and bob are friends!!!
splitList=strSp.split()
print("split List elements are :",splitList) #split List elements are : ['Alise', 'and', 'bob', 'are', 'friends!!!']
print("splitList type is ",type(splitList))  #splitList type is  <class 'list'>
print("strSp type is ",type(strSp))          #strSp type is  <class 'str'>

print("**************************************************************************************************************************************************************")

#Nested list concept:: List can contain another list example: l=[10,20,[30,40]]

#create no of list using list() and for loop

print("**************************************************************************************************************************************************************")
# Accesing elements of list by using index or by using slice operator
# index: have +ve or -ve index
# if using index use with in the range otherwise it leads to error "index error: list index out of range"

indList=eval(input("Enter a list"))                     #Enter a list[198,'alice','_#']
print("Just print indList\n",indList)                   # Just print indList
                                                        # [198, 'alice', '_#']


print("print list using forloop")
for x in indList:
    print(x)
#print list using forloop
#198
#alice
#_#

#print("List of elements are : ", indList)
print("print list using forloop with range and len() (which is a +ve index)")
for x in range(len(indList)):
    print(indList[x])
#print list using forloop with range and len() (which is a +ve index)
#198
#alice
#_#

print("print a list of elements in reverse order without using buit-in function and slice operator")
for x in range(len(indList)-1,-1,-1):
    print(x,'\t',indList[x])
#print a list of elements in reverse order without using buit-in function and slice operator
#2 	 _#
#1 	 alice
#0 	 198

#enumerate() returns an enumerate object example <enumerate object at 0x0511D2B0> using for loop we can access the index and the context of a list
print("List with index and context using enuumerate()")
for index,value in enumerate(indList):
    print (index,value)
#List with index and context using enuumerate()
#0 198
#1 alice
#2 _#



# Slice operator syntax is list[begin:end:step]
# step can be +ve or -ve index where +ve index means forward direction and -ve index means backward direction

# print list of elements using slice operator
print("empty list using slice operator")
l=[]
print("list l is \t",l[::])                                         #list l is 	 []

lSlice=eval(input("Enter the list of elements"))                    #Enter the list of elements[10,'alice']
print("Length of elements in the list lSlice : \t", len(lSlice))    # Length of elements in the list lSlice : 	 2
print("list of elements with slice operator using forward direction : \n",lSlice[:len(lSlice):1])     #list of elements with slice operator using forward direction :
                                                                                                      #[10, 'alice']
# forward slicing using for loop    
print("list of elements with slice operator using forward direction : \n",lSlice[::-1])

# access required list elements using with or without slice operator
# dynamic way of entering elts into list using for loop




#Exercises¶
#First List - Loop
    #Repeat First List, but this time use a loop to print out each value in the list.
#First Neat List - Loop
    #Repeat First Neat List, but this time use a loop to print out your statements. Make sure you are writing the same sentence for all values in your list. Loops are not effective when you are trying to generate different output for each value in your list.
#Your First List - Loop
    #Repeat Your First List, but this time use a loop to print out your message for each item in your list. Again, if you came up with different messages for each value in your list, decide on one message to repeat for each value in your list.

 # print a list in reverse order using slice operator    ---> hint y = x[::-1]


#help urls for list
    #http://introtopython.org/lists_tuples.html#Lists-and-Looping
    
    



why interpreter is not showing error msg for _ underscore but in the case of other special character it is giving error msg like SyntaxError

>>> type(_)
<class 'type'>

>>> type($)
SyntaxError: invalid syntax


for i in l1:
	print(type(exL[i]))

TypeError: 'int' object is not iterable

for i in range(0,n):


create no of list using list() and for loop
step=0
for i in range(0,10,step):
    print("list elements",lFun)                 









      
