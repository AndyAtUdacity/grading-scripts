def addOdds(int1, int2):
	if int1 < int2:
		big = int2
		small = int1
	elif int1 == int2:
		return 0
	else:
		big = int1
		small = int2
	sum = 0
	for i in range(small+1, big):
		if i % 2 == 1:
			sum += i
	return sum

print addOdds(3,-5)
print addOdds(-20, -20)