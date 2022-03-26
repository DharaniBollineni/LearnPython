# pop() means in the stack it is used in top most or last most element
# remove() won't return any thing
#pop() it removes last element and returns that element
#pop() method returns IndexError: pop from empty list 
#note:
# function is written outside the class eg: len()
# function is written inside the class is called method, if calling a funtion using an object is called as method eg: extend()

pl1=[101,'alice','pop','0.0.0.0','log.txt']
print('list before using pop()',pl1)
print('pop 1st element',pl1.pop())
print('pop 2nd element',pl1.pop())
print("list after poping element",pl1)

# Wap to check list is empty to perfrom pop operation
# To remove specifed element
pL2=[]
if len(pL2)==0:
    print("List is empty Can't perform pop operation")
else:
    pL2.pop()
    print("list after poping elements from the list",pL2)
#output: List is empty Can't perform pop operation

#

