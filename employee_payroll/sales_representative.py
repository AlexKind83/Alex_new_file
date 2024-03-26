from employee_payroll.salary_employee import SalaryEmployee


class SalesRepresentative(SalaryEmployee):
    def __init__(self, id_name, name, weekly_salary, commission_salary):
        super().__init__(id_name, name, weekly_salary)
        self.commission_salary = commission_salary

    def calculate_payroll(self):
        return self.weekly_salary + self.commission_salary
