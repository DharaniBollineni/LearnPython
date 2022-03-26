#
ichr=input("Enter any characters:")
#count=0
if ichr.isalnum():
    print(ichr," is alpha numaric character")
    #count= count+1
    if ichr.isalpha(): #& count==1:
        print(ichr," is alphabet character")
        if ichr.islower():
            print(ichr," is lowercase character")
        else:
            print(ichr," is uppercase character")
    else:
        print(ichr," is a digit")
elif ichr.isspace():
    print(ichr," is a space character")
else:
    print(ichr," is a non but a space special character")
        
