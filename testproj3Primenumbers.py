#index with try and except
mfList=[10,20,30,30,40,10,'A','B','b','()']
target=eval(input("Enter the search item     "))
print(type(target))
try:
    print(target," is available are index ",mfList.index(target))
except ValueError:         #except Error:
    print(target," is not available")                                                   

#cas21: if I enter serach as b (not 'b') then resulting as NameError: name 'b' is not defined
    # for more information check below
#Enter the search item     b
#Traceback (most recent call last):
 # File "C:\Users\HP-Test\Desktop\Python\testproj3Primenumbers.py", line 3, in <module>
  #  target=eval(input("Enter the search item     "))
  #File "<string>", line 1, in <module>
#NameError: name 'b' is not defined
#My question is
#We are using eval() with input() ideally it should be string type as per the below example why is not considering as string
#>>> a=input("data")
#data dfsd
#>>> type(a)
#<class 'str'>

  




# WAP to find the position of item in the list
        # if available return position/index
        # if not available handle the exception





iList2=['a','e','i']#eval(input("Enter a list"))
target=eval(input("Enter the item to be searched"))
#l.index(search)
try:
    print(target," is available at the index ",iList2.index(target))
except ValueError:
    print("Item is not available")

