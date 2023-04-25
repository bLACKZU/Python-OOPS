class Employee:

    raise_amt = 1.08
    no_of_employees = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
       
    def fullName(self):
        return '{}-{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt
       
   
class Developer(Employee):

    raise_amt = 1.09
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
       
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(emp.fullName())

dev_1 = Developer("Satyaki", "Ghosh", 50000, "Python")
mgr_1 = Manager("Jack", "Sparrow", 80000, [dev_1])

print(mgr_1.print_emp())
