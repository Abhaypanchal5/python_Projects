def star(n):
    i = 1
    for i in range(1,n+1):
        print(" "*(n-i + 1),"*"*i + "*"*(i-1)+" "*(((n*2)+1)-(i*2))+"*"*i + "*" *(i-1))
        i =+ 1
    
    for i in range(n-1,0,-1):
        print(" "*(n-i + 1),"*"*i + "*3"*(i-1)+" "*(((n*2)+1)-(i*2))+"*"*i + "*"*(i-1))
        i =+ 1
        
a = int(input("Enter the number of row you want in your piramid: "))
star(a)
star(a)