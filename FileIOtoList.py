file1 = open("example.txt","r")
lst = file1.readlines()
for i in range(len(lst)):
	lst1.append(lst[i].rstrip('\n').split(' '))
lst1 = [[int(x) for x in lst2] for lst2 in lst1]