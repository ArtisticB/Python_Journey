n=int(input("Give The Number Till Which You Want To Take Prime Numbers:"))

for i in range (2,n):
    flag = False
    
    for num in range (2,i):
        
        if i%num==0:
            flag = True
            
    if not flag:    #if flag=False
               print(i)