n=int(input())
l=list(map(int,input().split()))
l.remove(max(l))
l.remove(min(l))
lt=len(l)

for i in range(lt):
    total=sum(l)/lt
    h=format(total,".8f")
print(h)
    
    
