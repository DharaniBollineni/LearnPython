print("# split with default value")
s="durga soft solutions"
print(s)
l=s.split()
print(l)
for x in l:
    print(x)
    

print("# split() with -")
s="02-03-3018"
l=s.split('-')
print(l)
for x in l:
    print(x)

print("# split() with limit")
s="Durga software solutions hyd india"
print(s)
l=s.split(' ',3)
print(l)
for x in l:
    print(x)

print("# rsplit() with limit")
s="Durga software solutions hyd india"
print(s)
l=s.rsplit(' ',3)
print(l)
for x in l:
    print(x)

print("# split() with limit")
s="10,20,30,40,50,60"
print(s)
l=s.split(',',3)
print(l)
for x in l:
    print(x)

print("# rsplit() with limit")
s="10,20,30,40,50,60"
print(s)
l=s.rsplit(',',3)
print(l)
for x in l:
    print(x)

print("# rsplit() with ,")
# rsplit() 
s="10,20,30,40,50,60"
print(s)
l=s.rsplit(',')
print(l)
for x in l:
    print(x)


print("# rsplit() default value is -1")
s="10,20,30,40,50,60"
print(s)
l=s.rsplit(',',-1)
print(l)
for x in l:
    print(x)

print("# rsplit() with space")
s="10 20 30 40 50 60"
print(s)
l=s.rsplit(' ')
print(l)
for x in l:
    print(x)
