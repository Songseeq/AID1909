
res = list(map(lambda x:x**3,list(filter(lambda x:True if x % 2 == 0 else False,range(11)))))
print(res)

print(reduce(lambda x,y:x+y , [1,2,3,4,5]))

