# WAP to diaplay all positions of substring in the given main string (no of times substring in Main string with its index

mStr=input("Enter main string")
sStr=input("Enter substring")
flag=False
pos=-1
count=0
n=len(mStr)
while True:
    pos=mStr.find(sStr,pos+1,n)
    if pos==-1:
        break
    print("found index",pos)# ,count=count+1)
    flag=True
    count=count+1
if flag==False:
    print("Not found")
else:
    print(sStr," is available for ",count," times")



# count() to find count of occurence
#string.count(substring)
'abababab'.count('ab')


# simple one
string=input("Enter string:")
sub_str=input("Enter word:")
if(string.find(sub_str)==-1):
      print("Substring not found in string!")
else:
      print("Substring in string!")


#wap for Count the overlapping occurance of a substring in Python  
