# Enter your code here. Read input from STDIN. Print output to STDOUT

q = int(input())

stackPush = []
stackDelete = []

for i in range(q):
    t = list(input().split())
    
    if t[0] == "1":
        stackPush.append(t[1])
        
    elif t[0] == "2":
        if not stackDelete:
            while stackPush:
                stackDelete.append(stackPush.pop())
        stackDelete.pop()
           
    else:
        if not stackDelete:
            while stackPush:
                stackDelete.append(stackPush.pop())
        print(stackDelete[-1])
                