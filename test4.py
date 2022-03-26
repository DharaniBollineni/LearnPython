#remove()
#list.remove(element) and holds a single element has an argument
#if passed element is available then remove() method removes the element from the list
#if passed element doesn't exist then remove()method returns ValueError Exception.

#Basic details about remove()
#port=99
rList=['alice','bob','190.99.101.99',10,99]
print("Actual List is ",rList)
rElement=eval(input("Enter the element"))
print(rElement)
try:
    rLsit.remove(rElement)
    print("List after removing element from the list",rList)
except:
    print("remove element is not available")
print(rList)

# whats worng in my program not able to remove element from the list   
#case1:
#Actual List is  ['alice', 'bob', '190.99.101.99,10', 99]
#Enter the element'bob'
#remove element is not available
#case2:
#Actual List is  ['alice', 'bob', '190.99.101.99,10', 99]
#Enter the elementbob
#remove element is not available

