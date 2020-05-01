class AssignmentFive():
    def __init__(self):
        self.loan_payment = 0
        self.insurance = 0
        self.oil = 0
        self.tires = 0
        self.maintenance = 0
    
    def main(self):
        self.loan_payment = input('enter monthly loan payment: ')
        self.insurance = input('enter monthly gas payment: ')
        self.oil = input('enter monthly oil payment: ')
        self.tires = input('enter monthly tires payment: ')
        self.maintenance = input('enter monthly maintenance payment: ')
    
    def showExpenses(self, loan_payment, insurance, oil, tires, maintenance):
        total_monthly = int(self.loan_payment) + int(self.insurance) + int(self.oil) + int(self.tires) + int(self.maintenance)
        total_annual = total_monthly * 12 
        print('The total monthly expenses is ',total_monthly)
        print('The total annual expenses is ',total_annual)
        

    def maximum(self, first, second):
        if(first > second):
            return first
        elif (second > first):
            return second
        else: #equal, doesnt matter
            return first
    
    #was not able to get question 3 but this was my logic
    
    def add_digits(self, original):
        return_val = 0
        if(return_val < 10 and return_val != 0):
            return return_val
        else:
            recursive = AssignmentFive.sum_digits(original)
            add_digits(recursive)
    
    #taken from stack overflow
    def sum_digits(self, number):
        out = 0
        while number:
            out += number % 10
            number //= 10
        return out

                




    

        


