from employee_payroll.employee import Employee


class HourlyEmployee(Employee):
    """Сотрудники с почасовой зарплатой"""
    def __init__(self, id_name, name, hours_worked, hour_rate):
        super().__init__(id_name, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate
