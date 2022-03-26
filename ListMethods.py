# important functions and methods of list
#len(list)--> method
#count( )--> method-->how many times this object is available         
#index() --> first occurance of given elt in list
               # if available the gives index of first occurance
               # else give ValueError :: ValueError: value is not in list
print("----------------------------------------------------------------------------------------------------------------------")
a=10
mfList=[10,20,30,30,40,10,'A','B','a','()',a]
#len() method
print("Legnth of list is ",len(mfList))                                                   #Legnth of list is  11
#count() method
print("count of string 'A' in list ", mfList.count('A'))                                  #count of string 'A' in list  1
print("count of 10 in list ", mfList.count(10))                                           #count of 10 in list  3
print("count of a in list ", mfList.count(a))                                             #count of a in list  3
#index() method
print("index of 30 in list",mfList.index(30))                                             #index of 30 in list 2

print("----------------------------------------------------------------------------------------------------------------------")
# details to know about index every element in the list is access by index
# index starts with 0 and ends as len(list)-1
#index() method takes single argument(search element)
        # if found returns index of the search element
                #only the first index of the element is printed
        # if not found returns ValueError exception indicating the element not available in the list
print("----------------------------------------------------------------------------------------------------------------------")

# WAP to print index of every item in the list
log='logfile.txt'
iList=[999,'non',log,'a''b','!@#',[],[1,2,3,4]]
for x in iList:
    print("{}   item is at the position/index   {}".format(x,iList.index(x)))

#output:
#999   item is at the position/index   0
#non   item is at the position/index   1
#logfile.txt   item is at the position/index   2
#ab   item is at the position/index   3
#!@#   item is at the position/index   4
#[]   item is at the position/index   5
#[1, 2, 3, 4]   item is at the position/index   6

print("----------------------------------------------------------------------------------------------------------------------")


# index with input value
target=eval(input("Enter the value to search"))
if target in mfList:
    print(target," is available are index ",mfList.index(target))
else:
    print(target," is not available")
#output:
#Enter the value to search 40
#40  is available are index  4

print("----------------------------------------------------------------------------------------------------------------------")
        
#index with try and except
target=eval(input("Enter the value to search"))                                         #Enter the value to search 98

try:
    print(target," is available are index ",mfList.index(target))
except ValueError:         #except Error:
    print(target," is not available")                                                   #98  is not available

print("----------------------------------------------------------------------------------------------------------------------")

    
#Manipulation elements of list
#--------------------------------------------------------------------------
#list.append(item)--> add item to list                      ---> added list to list forms nested list
#list.insert(index,item)-->insert item @ specified location/index position
#extand() --> add all items to list
        #-->list1.extend(list2)
        #--> added list to list appends list2 to list1 itself(extended list)
        #--> extend: Extends list by appending elements from the iterable.
                          
#Basic list append method
apList1=[]
apList1.append(10)
apList1.append(20)
apList1.append(30)
print("apList elts",apList1)                                                            #apList elts [10, 20, 30]
print("----------------------------------------------------------------------------------------------------------------------")

#append a existed list
apListA1=['Alice','bob','kate']
apListA1.append('eve')
print("updated list is ",apListA1)                                                      #updated list is  ['Alice', 'bob', 'kate', 'eve']

print("----------------------------------------------------------------------------------------------------------------------")

#add list to list
apListA2=['alice','bob']
apListA3=['charli','eve']
apListA2.append(apListA3)
print("updated list is ",apListA2)                                                      #updated list is  ['alice', 'bob', ['charli', 'eve']]

print("----------------------------------------------------------------------------------------------------------------------")

#note: If you need to add items of a list to the another list (rather than the list itself), extend() method is used.
apListA2=['alice','bob']
apListA3=['charli','eve']
apListA2.extend(apListA3)
print("updated list is ",apListA2) #updated list is  ['alice', 'bob', 'charli', 'eve']

apList1A3=[10,20,30]
apList2A3=[40,50,60]
apList1A3.extend(apList2A3)
print(apList1A3)
print("----------------------------------------------------------------------------------------------------------------------")

#WAP add all elt to list upto 100 which are divisible by 5
apList2=[]
for x in range(101):
    if x % 5==0:
        apList2.append(x)
print("Elments divisable with 5",apList2)                                               #Elments divisable with 5 [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
print("----------------------------------------------------------------------------------------------------------------------")

# WAP to insert elt @ specified location/index position
apList3=[]
apList3.append(10)
apList3.append(20)
apList3.append(30)
print("apList elts",apList3)                                                            #apList elts [10, 20, 30]
apList3.insert(1,50)
print("apList elts after insertion",apList3)                                            #apList elts after insertion [10, 50, 20, 30]
print("----------------------------------------------------------------------------------------------------------------------")

# note if index > len(list) then added at last
#       if index <0 then add elt at begining
apList3.insert(30,1000)
apList3.insert(-30,2000)
print("apList elts after insertion index > len(list) and index<0",apList3)
print("index(1000)",apList3.index(1000))
print("index(2000)",apList3.index(2000))

# output:
#apList elts after insertion index > len(list) and index<0 [2000, 10, 50, 20, 30, 1000]
#index(1000) 5
#index(2000) 0

print("----------------------------------------------------------------------------------------------------------------------")
    

apList1A3=[10,20,30]
apList2A3=[40,50,60]
print("apList1A3 is ",apList1A3)
print("apList2A3 is ",apList2A3)
apList1A3.extend(apList2A3)
print("List after appending  2ndlist to 1st lsit ",apList1A3)

#apList1A3 is  [10, 20, 30]
#apList2A3 is  [40, 50, 60]
#List after appending  2ndlist to 1st lsit  [10, 20, 30, 40, 50, 60]

print("----------------------------------------------------------------------------------------------------------------")
#append adds complete value to the list
 
l1=[]
l2=[]
apWExList1=[10,20,30,40]
l1.append('Alice')
l2.extend('alice')
print("List with append",l1)
print("List with extend",l2)

print("----------------------------------------------------------------------------------------------------------------")
#
#List with append ['Alice']
#List with extend ['a', 'l', 'i', 'c', 'e']


# remove(): the specifed element by default will be deleted and remove() won'tt return any thing 
# basic remove() use: direct remove an element from the lsit 
l1=[10,20,'keeth']
print("l1 before removing from the list",l1)
l1.remove(10)
print("after removing integer 10 from the list",l1)
l1.remove('keeth')
print("after removing string'keeth' from the list",l1)
#l1 before removing from the list [10, 20, 'keeth']
#after removing integer 10 from the list [20, 'keeth']
#after removing string'keeth' from the list [20]


#remove a specified element from the list 
l2=[505,'404','100.99.99.99','bob']
print("l2 is ",l2)
x=eval(input("Enter an element from the list with in l2"))
print("given element is ",x)
l2.remove(x)
print("list after removing element from the list is ",l2)

#l2 is  [505, '404', '100.99.99.99', 'bob']
#Enter an element from the list with in l2 '100.99.99.99'
#given element is  100.99.99.99
#list after removing element from the list is  [505, '404', 'bob']

#l2 is  [505, '404', '100.99.99.99', 'bob']
#Enter an element from the list with in l2 505
#given element is  505
#list after removing element from the list is  ['404', '100.99.99.99']

print("----------------------------------------------------------------------------------------------------------------")
#remove an element if element is available otherwise print a messgae like given element is not available
l4=[102,'202','999.999.999.999','alice']
print("l4 is ",l4)
x=eval(input("Enter an element"))
print("given element is ",x)
if x in l4:
    l4.remove(x)
    print("Element is succesfully deleted")
    print("list after removing element from the list is ",l4)
else:
    print("specifed element is not available")

#l4 is  [102, '202', '999.999.999.999', 'alice']
#Enter an element202
#given element is  202
#specifed element is not available

#l4 is  [102, '202', '999.999.999.999', 'alice']
#Enter an element'999.999.999.999'
#given element is  999.999.999.999
#Element is succesfully deleted
#list after removing element from the list is  [102, '202', 'alice']

#Note:
#------------------------------------------------------------------------------------
# error message for remove()
# if specifed element is not available then we get ValueError
#l3=[10,20,'alice','bob']
#l3.remove('10.99.999.999')
#Traceback (most recent call last):
#  File "<pyshell#9>", line 1, in <module>
#    l3.remove('10.99.999.999')
#ValueError: list.remove(x): x not in list




