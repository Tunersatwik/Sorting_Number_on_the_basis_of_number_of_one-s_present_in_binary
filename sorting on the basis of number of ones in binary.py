print('Enter NO. of Test Case:')
t=int(input())
while(t):
    print('Give your Sequence')
    arr=list(map(int,input().split()))
    dic_num={}
    for item in arr:
        b=bin(item)
        b.replace('0b','')
        t=b.count('1')
        dic_num[item]=t
    d=sorted(dic_num.items(), key= lambda kv:(kv[1], kv[0]))
    print(d)
    a=[]
    for item in d:
        a.append(item[0])
    print(a[::-1])
    t-=1
