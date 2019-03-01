l1=[1,2,3]
l2=[1,2,3,4]

for i in l2:
	if i not in l1:
		l1.append(i)
	
print(l1)