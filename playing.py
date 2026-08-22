l = [4, 5, 1, 2, 9, 7, 10, 8]
print("orginal list:",l)
count = 0
for i in l:
    count += i
avg = count / len(l)
print("sum of list=",count)
print("average =",avg)
l.sort()
print("smallest element is:",l[0])
print("largest element is:",l[-1])