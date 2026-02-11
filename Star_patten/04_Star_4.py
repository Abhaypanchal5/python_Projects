def star(n):
    i = 1
    for i in range(1,n+1):
        print(" "*(n-i + 1),"*"*i + "*"*(i-1))
        i =+ 1
        
n = int(input("Enter the number of row you want in your piramid: "))
star(n)