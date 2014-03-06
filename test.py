from sets import Set

myset = Set([1,2,3,4,5]);
for x in myset:
	for y in myset:
		if y != x:
			# y is the index for training set, x is the test set
			print y
