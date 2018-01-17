#Calculator

in_file = open('C:/Users/HP/Desktop/test.txt','r')
ch = []
ch = in_file.read().split()
r=len(ch)
arr=[]
k=0
for i in  range(r):
    arr.append(ch[k])
    k=k+1
i=1
res=[]
while i<r :
    if arr[i]=='+':
        res.append((float)(arr[i-1]) + (float)(arr[i+1]))
    if arr[i]=='-':
        res.append((float)(arr[i+1]) - (float)(arr[i-1]))
    if arr[i]=='*':
        res.append((float)(arr[i-1]) * (float)(arr[i+1]))
    if arr[i]=='/':
        res.append((float)(arr[i-1]) / (float)(arr[i+1]))
    i=i+3
r = len(res)
i=0
for i in range(r):
    print(res[i])
    
