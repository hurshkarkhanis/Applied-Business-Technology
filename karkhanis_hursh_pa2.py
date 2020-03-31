numMale = input("How many males are in the class? ")

numFemale = input("How many females are in the class? ")

malePCT = float (numMale)/(numMale+numFemale) * 100
femalePCT = float (numFemale)/(numMale+numFemale) * 100

print "MALE PERCENTAGE: ", round(malePCT, 2), "%"
print "FEMALE PERCENTAGE: ", round(femalePCT, 2), "%"


subtotal = input("How much was your resaturant bill? ")

tip = float(subtotal*0.18)

if tip < 2:
	tip = 2

print "Subtotal: $", subtotal
print "Tip:      $", tip
print "Total     $", subtotal + tip


bagelOrder = input("How many bagles do you want to order? ")

lessThanHalf = 0.75
moreThanHalf = 0.60

costPer = 0

if bagelOrder < 12:
	totalCost = float (bagelOrder * lessThanHalf)
	costPer = lessThanHalf
if bagelOrder >= 12:
	totalCost = float (bagelOrder * moreThanHalf)
	costPer = moreThanHalf;

print "Number of Bagles Ordered: ", bagelOrder
print "Cost per Bagel: ", costPer, "c"
print "Total Cost: $", totalCost

