import math

age = input('enter age in full years: ')
classification = ''
if age <= 1:
	classification = 'infant'
else:
	if age > 1 and age < 13:
		classification = 'child'
	else: 
		if age >= 13 and age < 20:
			classification = "teenager"
		else:
			classification = 'adult'

print "this child is a/an:  ", classification



year = input('enter a year: ')
leap = False

if year % 100 == 0 and year % 400 == 0:
	leap = True
if year % 100 != 0 and year % 4 == 0:
	leap = True

if leap:
	print 'In ', year, ", February has 29 days."
else:
	print 'In ', year, ", February has 28 days."



currentPop = 7000000000
goalPop = 	8000000000
yearCount = 2011

while currentPop < goalPop:
	print yearCount, ':', currentPop
	currentPop = currentPop*(1.011)
	yearCount = yearCount + 1


	
print 'Population will hit 8 billion in year', yearCount


budget = input('enter monthly budget: ')
done = False
totalSpending = 0
while done == False:
	dataPoint = input('enter expense, or enter 0 to end month ')
	if(dataPoint == 0):
		done = True
	else:
		totalSpending = totalSpending + dataPoint
print
print "total spending: $", totalSpending
print

if totalSpending > budget:
	print "you are $", (totalSpending-budget), ' over budget. you should cut down!'
else:
	if totalSpending < budget:
		print "you are $", (budget-totalSpending), ' under budget. good job!'
	else:
		if totalSpending == budget:
			print "you broke even for the month."






 













