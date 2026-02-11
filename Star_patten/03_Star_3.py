def Star(n):
    i = 1
    while i <= n:
        print(" "*(n-i + 1),"*"*i + "*"*(i-1))
        i += 1
n = int(input("Enter the number of row you want in your piramid: "))
Star(n)