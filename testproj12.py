 
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


