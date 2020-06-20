lst1, signup, bookship, libeff, books, books1, bookseq, emptylib, libseq = [], [], [], [], [], [], [], [], []
libcount = 0
file1 = open("a_example.txt","r")
lst = file1.readlines()
for i in range(len(lst)):
	lst1.append(lst[i].rstrip('\n').split(' '))
lst1 = [[int(x) for x in lst2] for lst2 in lst1]
print(lst1)
l = len(lst)
#save signup and ship count in separate arrays
for i in range(2,l):
	if(i%2==0):
		signup.append(lst1[i][1])
		bookship.append(lst1[i][2])
#calculate combined efficiency for signup days and ship count and store
for j in range(0,lst1[0][1]):
	libeff.append(signup[j]*bookship[j])
print(libeff)
#decide most efficient library by ascending libeff values
libeffsort = [i[0] for i in sorted(enumerate(libeff), key=lambda x:x[1])]
print(libeffsort)
#getting books from libraries based on efficiency
#storing library books in separate array
for i in range(2,l):
	if(i%2!=0):
		books.append(lst1[i])
print(books)
#reordering books array as per library efficiency from libeffsort
for i in libeffsort:
	books1.append(books[i])
print(books1)
#generating the book sequence per library
tmp = books1
for i in range(0,lst1[0][1]):
	bookseq.append(tmp[i])
	tmp = [[x for x in ls if not (x in books1[i])] for ls in tmp]
print(bookseq)
#count no of libraries resulting to be scanned
for i in range(lst1[0][1]):
	if(len(bookseq[i])>0):
		libcount += 1
	else:
		emptylib.append(i)
print(libcount)
#get library sequence if changes due to common books
libseq = [i for n, i in enumerate(libeffsort) if n not in emptylib]
print(libseq)
#have all that is needed so now to present it as asked