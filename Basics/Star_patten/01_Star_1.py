n =  int(input("Enter the number of rows you want in your piramind : "))

i = 1
for i in range(1,n+1):
    print(" "*(n-i + 1),"*"*i + "*"*(i-1))
    i += 1