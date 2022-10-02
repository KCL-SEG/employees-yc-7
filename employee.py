"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class SalaryEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return str(self.name) + " works on a monthly salary of " + str(self.salary) + ".  Their total pay is " + str(self.get_pay())+"."

class contractEmployee(Employee):
    def __init__(self, name, paymentPerHour, hoursWorked):
        super().__init__(name)
        self.paymentPerHour = paymentPerHour
        self.hoursWorked = hoursWorked

    def get_pay(self):
        return self.paymentPerHour * self.hoursWorked

    def __str__(self):
        return str(self.name) + " works on a contract of " + str(self.hoursWorked) +" hours at " + str(self.paymentPerHour) + "/hour.  Their total pay is " + str(self.get_pay()) +"."

class SalaryCommissionPerContractEmployee(SalaryEmployee):
    def __init__(self, name, salary, numContracts, commissionPerContract):
        super().__init__(name, salary)
        self.numContracts = numContracts
        self.commissionPerContract = commissionPerContract

    def get_pay(self):
        return self.salary + self.numContracts*self.commissionPerContract

    def __str__(self):
        return str(self.name)+" works on a monthly salary of "+str(self.salary)+" and receives a commission for "+str(self.numContracts)+" contract(s) at " +str(self.commissionPerContract)+"/contract.  Their total pay is "+str(self.get_pay()) + "."

class ContractCommissionPerContractEmployee(contractEmployee):
    def __init__(self, name, paymentPerHour, hoursWorked, numContracts, commissionPerContract):
        super().__init__(name, paymentPerHour, hoursWorked)
        self.numContracts = numContracts
        self.commissionPerContract = commissionPerContract

    def get_pay(self):
        return super().get_pay() + self.numContracts*self.commissionPerContract

    def __str__(self):
        return str(self.name) + " works on a contract of " + str(self.hoursWorked) +" hours at " + str(self.paymentPerHour) + "/hour and receives a commission for "+str(self.numContracts)+" contract(s) at "+str(self.commissionPerContract)+"/contract."  +"  Their total pay is " + str(self.get_pay()) +"."

class SalaryCommissionEmployee(SalaryEmployee):
    def __init__(self, name, salary, commission):
        super().__init__(name, salary)
        self.commission = commission

    def get_pay(self):
        return super().get_pay() + self.commission

    def __str__(self):
        return str(self.name) + " works on a monthly salary of " + str(self.salary) +" and receives a bonus commission of "+ str(self.commission) + ".  Their total pay is " + str(self.get_pay())+"."

class ContractCommisionEmployee(contractEmployee):
    def __init__(self,name, paymentPerHour, hoursWorked, commission):
        super().__init__(name, paymentPerHour, hoursWorked)
        self.commission = commission

    def get_pay(self):
        return super().get_pay() + self.commission

    def __str__(self):
        return str(self.name) + " works on a contract of " + str(self.hoursWorked) + " hours at " + str(self.paymentPerHour) + "/hour and receives a bonus commission of "+str(self.commission)+".  Their total pay is " + str(self.get_pay()) + "."



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie',salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = contractEmployee('Charlie',paymentPerHour=25,hoursWorked=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryCommissionPerContractEmployee('Renee', salary=3000, numContracts=4, commissionPerContract=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractCommissionPerContractEmployee('Jan', paymentPerHour=25, hoursWorked=150, numContracts=3, commissionPerContract=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryCommissionEmployee('Robbie', salary=2000, commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractCommisionEmployee('Ariel', paymentPerHour=30, hoursWorked=120, commission=600)
