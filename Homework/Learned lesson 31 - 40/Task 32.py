from employee_payroll.salary_employee import SalaryEmployee
from employee_payroll.hourly_employee import HourlyEmployee
from employee_payroll.sales_representative import SalesRepresentative
from employee_payroll.payroll_system import PayrollSystem


salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
sales_representative = SalesRepresentative(3, "Николай Хорольский", 1000,
                                           250)

payroll_system = PayrollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee,
    sales_representative
])
