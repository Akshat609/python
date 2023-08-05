#Collatz sequence -> divide by 2 if number is even amd use 3n+1 if number is odd


n = int(input("enter a integer "))
a = n
i=0

print(f"Collatz conjecture: {n}", end="") #escape sequence end="" is used to diable the inbuilt new line character
while a>1:
    i = i+1
    if(a%2 == 0):
        a = a/2
    else:
        a = 3*a + 1
    
    print(f" {int(a)}", end="")
    
print(f"\n Iterations {i}")





