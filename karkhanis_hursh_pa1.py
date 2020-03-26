
revenue = input("what are you annual sales in dollars? ")

profitRate = input("what is your profit margin? ")

totalProfit = revenue * profitRate

print 

print 'total profit: ', totalProfit

print


subtotal = input("what did your meal cost? ")
tip = subtotal * 0.18
tax = subtotal * 0.07

print 'subtotal : ', subtotal
print 'tip : ', tip
print 'tax : ', tax
finalBill = subtotal+ tip+ tax
print 'total bill : ', finalBill

print




print "this is what you will need for 48 cookies:"
sugarCups = 1.5
butterCups = 1
flourCups = 2.75
print "1.5 cups of sugar"
print "1 cup of butter"
print "2.75 cups of flour "

numberOfCookiesNeeded = input ("how many cookies do you want to make? ")

cookiesInAServing = 48

servings = (numberOfCookiesNeeded/cookiesInAServing)  #to make it easier

print "if you want ", numberOfCookiesNeeded, " cookies, you will need: "
print sugarCups * servings , "cups of sugar"
print butterCups * servings , "cups of butter"
print flourCups * servings , "cups of flour"










