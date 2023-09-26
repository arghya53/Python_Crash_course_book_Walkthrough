class Employee:

    def __init__(self, first_name, last_name, annual_income):

        self.first_name = first_name
        self.last_name = last_name
        self.annual_income = annual_income
    
    def give_raise(self, raise_amount = 5000):
        self.annual_income += raise_amount
        # print(f"{}")

employee = Employee('Arghya', 'Biswas', 50000)

print(employee.annual_income)
