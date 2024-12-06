t = int(input())


for _ in range(t):

    n = int(input())
    
    
    result = []
    

    for i in range(n):
        row = input().strip()
        
        column = row.index('#') + 1
        result.append(column)
    
   
    print(" ".join(map(str, result[::-1])))