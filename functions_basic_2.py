def countdown(num):
    for i in range(num,-1, -1):
        print(i)
        
countdown(5)

def printReturn (a,b):
    print(a)
    return(b)

x=printReturn(1,2)
print(x)

def firstLength (num):
    x = num[0] + len(num)
    print(x)

num=[1,2,3,4,5]
firstLength(num)

def valueGreatersecond (lis):
    if len(lis) < 2:
        return False
    x = []
    for i in range(0, len(lis)):
        if lis[i] > lis[1]:
            x.append(lis[i])
    print(len(x))
    return x


print(valueGreatersecond([5,2,3,2,1,4]))
print(valueGreatersecond([3]))

def lengthValue(a,b):
    output=[]
    for i in range (0, a):
        output.append(b)
    return output

print(lengthValue(4,7))
print(lengthValue(6,2))