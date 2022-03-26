#slice
print("Reversing using slicing operator")
sStr=input("Enter a string\n")
print(sStr[::-1])
      
#reverse with join
print("Reverse a string using reverse() with join")
rStr=input("Enter a string to be reversed\n")
# print(reversed(rStr)) ---> returns a "reversed objects" --->  <reversed object at 0x05CD7450>
for x in reversed(rStr):
    print(x,end='')
    
print("\nreverse with join()")
print(''.join(reversed(rStr)))
   
#using while loop
iStr=input("Enter a string\n")
l=len(iStr)-1
output=''
while l>=0:
    output=output+iStr[l]
    l=l-1
print(output)


#program 2: reversing the order of words
#input: Durga software solutions
#output: Solutions software Durga
iStr=input("\nEnter a sentences 2\n")
lt=iStr.split()
print(lt)
lt1=[]
l=len(lt)-1
while l>=0:
    lt1.append(lt[l])
    l=l-1
print(lt1)
output= ' '.join(lt1)
print(output)



#program3: reversing every word in the given string
#input: Durga software solutions
#output:agruD erawftos snoituluos

iStr=input("\nEnter a sentences2\n")
lt=iStr.split()
print(lt)
for x in lt:
    print(x[::-1],end=' ')

print("\nway2")
l1=[]
for x in lt:
    l1.append(x[::-1])
output=' '.join(l1)
print(output)

#program4:
#Enter a string and print even index and print odd index charactors.
sing slice and without slice operator

#program4:
#Enter a string and print even index and print odd index charactors.
#using slice and without slice operator

print("Enter a string and print even index and print odd index charactors")
iStr= input("Enter a string")
#with out Slice operator
i=len(iStr)-1
eIndexStr=[]
oIndexStr=[]
while i>=0:
    if i%2==0:
        eIndexStr.append(iStr[i])
    else:
        oIndexStr.append(iStr[i])
    i=i-1
eIndexStr=''.join(eIndexStr[::-1])
oIndexStr=''.join(oIndexStr[::-1])   
print("print even index and print odd index charactors using without slice") 
print("Even Index string ",eIndexStr)
print("Odd Index string ",oIndexStr)



# with slice operator
print("print even index and print odd index charactors using slice") 
eIndexStr=iStr[::2]
oIndexStr=iStr[1::2]
print("Even Index string ",eIndexStr)
print("Odd Index string ",oIndexStr)


#program 5:
#s1='RAVISOFT'
#s2='TEJA'
#output should be merjing two strings.RTAEVJIASOFT



#program 6:
#inputdata: B4A1D3
#outputdata: ABC134

#program 6:
#inputdata: a4b3c2
#outputdata: aaaabbbcc

#program 6:
#inputdata: a4k3b2
#outputdata: aeknbd

#a3z5
#abz$







































































