"""Complete this program to find the greatest produdct of five consecutive
digits in the list"""
#Opens file
in_file = open('array.txt')

#give us a empty variable. 
wholenumber = ''
count = 0
#read the contents of the in file and assign to our wholenumber variable
for r in in_file:
	#take each row and split into mini array. 
	row = r.split()
	for number in row:
		#check each number in the mini array and confirm is a digit not a empty string is letter we strip and white space and break returns
		if number and str(number.isdigit()):
			wholenumber += number.replace('\n','').strip()


#Make sure the wholenunmber is in a current format
print wholenumber

grand_total = 0
for i in xrange(0, len(wholenumber) -5):
	#reset current Total
	current_total = 1
	#grab the current string set
	current_string = tuple(wholenumber[i:i+5])
	#loops the current substring and gives temp total 
	for i in current_string:
		current_total *= int(i)
	#Compares the current total and then assign to grand total if bigger
	if current_total > grand_total:
		grand_total = current_total 

print 'The greatest produdct is {grand_total}. The numbers used are {current_string}'.\
       format(grand_total=grand_total,current_string=current_string)


