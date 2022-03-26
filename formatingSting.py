name=input("Enter the name: ")
age=input("Enter the age: ")
salary=input("Enter the salary ")

print("{}'s Age is {} and his salary is:{}".format(name,age,salary))
print("{0}'s Age is {1} and his salary is:{2}".format(name,age,salary))
print("{x}'s Age is {y} and his salary is:{z}".format(y=age,z=salary,x=name))
