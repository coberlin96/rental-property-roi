class Rental:
    def __init__(self):
        
        self.income = {}
        self.total_income = 0
        self.expenses = {}
        self.total_expenses = 0
        self.cash_flow = 0
        self.investment = {}
        self.total_investment = 0
        self.roi = 0.00

    def get_income(self):
        print("- - - - - INCOME - - - - -")
        
        rent = int(input("\nHow much do you plan to charge for rent? "))
        
        while True:
            renters = input("Will this property have more than one renter? (y/n) ")
            if renters.lower() == 'y':
                num = int(input("How many renters will there be? "))
                self.income['rent'] = rent * num
                break
            elif renters.lower() == 'n':
                self.income['rent'] = rent
                break
            else:
                print("Invalid input: please enter y or n for your answer")

        while True:
            additional = input("Do you plan to have any additional forms of income from this property? (y/n) ")
            if additional.lower() == 'y':
                new_source = input("What is the source of you additional income? ")
                new_amount = int(input("How much will you make through this? "))
                self.income[new_source] = new_amount
            elif additional.lower() == 'n':
                break
            else:
                print("Invalid input: please enter y or n for your answer")
        for source, amount in self.income.items():
            self.total_income += amount

        print(f"\nYour total montly income from this property is ${self.total_income}")


    def get_expenses(self):
        print("\n- - - - - EXPENSES - - - - -")
        tax = int(input("\nHow much will the property tax cost per month? "))
        self.expenses['tax'] = tax
        insurance = int(input("How much will the insurance cost per month? "))
        self.expenses['insurance'] = insurance
        vacancy = int(input("How much do you want to set aside for a future vacancy?(recomended: 5% of rent) "))
        self.expenses['vacancy'] = vacancy
        repair = int(input("How much will you be setting aside to handle small scale repairs/maintenance? "))
        self.expenses['repairs'] = repair
        capex = int(input("How much will you be setting aside to handle large scale repairs and replacements? "))
        self.expenses['capex'] = capex
        management = int(input("How much will you be paying for someone to manage your property? (0 if you're doing it yourself) "))
        self.expenses['management'] = management

        while True:
            utility = input('Will you be covering the utilities? (y/n) ')
            if utility.lower() == 'y':
                num = int(input("How much will this cost per month? "))
                self.expenses['utility'] = num
                break
            elif utility.lower() == 'n':
                break
            else:
                print("Invalid input: please enter y or n for your answer")

        while True:
            hoa = input("Is the property districted to a home owner's association? (y/n) ")
            if hoa.lower() == 'y':
                num = int(input("How much will this cost per month? "))
                self.expenses['hoa'] = num
                break
            elif hoa.lower() == 'n':
                break
            else:
                print("Invalid input: please enter y or n for your answer")

        while True:
            lawn = input('Will you be paying to have the lawn cut or otherwise cleared of things like snow? (y/n) ')
            if lawn.lower() == 'y':
                num = int(input("How much will this cost per month? "))
                self.expenses['lawn'] = num
                break
            elif lawn.lower() == 'n':
                break
            else:
                print("Invalid input: please enter y or n for your answer")

        while True:
            mortgage = input('Did you take out a mortgage to obtain this property? (y/n) ')
            if mortgage.lower() == 'y':
                num = int(input("How much do you is your monthly mortgage payment? "))
                self.expenses['mortgage'] = num
                break
            elif mortgage.lower() == 'n':
                break
            else:
                print("Invalid input: please enter y or n for your answer")

        while True:
            more = input('Is there any other monthly expenses from this property? (y/n) ')
            if more.lower() == 'y':
                new_source = input("What is the source of theis additional expenditure? ")
                new_amount = int(input("How much will this cost per month? "))
                self.expenses[new_source] = new_amount
                break
            elif more.lower() == 'n':
                break
            else:
                print("Invalid input: please enter y or n for your answer")
        
        for source, amount in self.expenses.items():
            self.total_expenses += amount

        print(f"\nYour toal monthly expenses for this property are ${self.total_expenses}")


    def get_investment(self):
        print("\n- - - - - INVESTMENT - - - - -")
        downpayment = int(input("\nHow much is the downpayment for this property? "))
        self.investment['downpayment'] = downpayment
        closing_cost = int(input("How much is the accumulated closing cost? (eg. lawyers, realters, appraisal) "))
        self.investment['closing_cost'] = closing_cost
        rehab = int(input("How much are you planning on budgeting to fix up the property before renting it out? "))
        self.investment['rehab'] = rehab
        while True:
            more = input('Is there any other one-time expenses you paid in getting this property? (y/n) ')
            if more.lower() == 'y':
                new_source = input("What is the source of this additional investment? ")
                new_amount = int(input("How much did it cost? "))
                self.investment[new_source] = new_amount
                break
            elif more.lower() == 'n':
                break
            else:
                print("Invalid input: please enter y or n for your answer")
        for source, amount in self.investment.items():
            self.total_investment += amount

        print(f"\nYour total investment in this property is ${self.total_investment}")
    
    def get_roi(self):
        self.cash_flow = self.total_income - self.total_expenses
        num = (self.cash_flow * 12) / self.total_investment
        self.roi = (num * 100)
        print(f"\nYour property's anual cash on cash ROI for this property is {self.roi}%")

    def run(self):
        self.get_income()
        self.get_expenses()
        self.get_investment()
        self.get_roi()

test = Rental()
test.run()

