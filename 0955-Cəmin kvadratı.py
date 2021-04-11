n=int(input())
m=n//1000
y=n//100%10
o=n%100//10
t=n%10
kv=(m+y+o+t)**2
print(kv)
