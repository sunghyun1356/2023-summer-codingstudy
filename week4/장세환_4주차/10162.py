t = int(input())
a, b, c = 0, 0 ,0 
if t % 10 != 0 :
    print(-1)
    exit()
else :
    a = t // 300
    b = (t % 300) // 60
    c = ((t % 300) % 60) // 10
print(a,b,c)