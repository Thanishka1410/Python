s="VIT"
t="Bhimavaram"
print(s+' '+t)
#triangular stars
n=int(input("enter a number"))
for i in range(n+1):
    print("*"*i)
#pyramid of stars
n=int(input("enter a number"))
for i in range(n+1):
    for j in range(n-i):
       print(" ",end="")
    for k in range(2*i-1):
       print("*",end="")
    print()

#string slicing
s="Thanishka"
t="Obilisetti"
n=len(s)
print(s[0:n])
print(s[0:3])
print(s[-1:n])
print(s[-1:n:2])
print(s[-1::-1])
print(s*3)
print(s +' '+t)
q=list(s.strip())
y="dog cat story"
print(q)
print(s.lower())
print(s.upper())
print(s.isupper())
print(s.islower())
print(y.capitalize())
print(y.title())



