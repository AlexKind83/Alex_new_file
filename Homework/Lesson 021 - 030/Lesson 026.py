
import re


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    SUFFIX = 'RUB'
    SUFFIX_USD = 'USD'
    SUFFIX_EUR = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.verify_surname(surname)
        self.verify_num(num)
        self.verify_percent(percent)

        self.__surname = surname
        self.__num = num
        self.__percent = percent
        self.__value = value
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт")
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт")

    def set_surname(self, surname):
        self.verify_surname(surname)
        self.__surname = surname

    def set_num(self, num):
        self.verify_num(num)
        self.__num = num

    def set_percent(self, percent):
        self.verify_percent(percent)
        self.__percent = percent

    def set_value(self, val):
        self.verify_value(val)
        self.__value = val

    def balance(self):
        print(f"Баланс счета: {self.__value} {self.SUFFIX}")

    def get_convert_to_usd(self):
        usd_val = self.__value * Account.rate_usd
        return print(f"Состояние счета: {usd_val} {Account.SUFFIX_USD}")

    def get_convert_to_eur(self):
        eur_val = self.__value * Account.rate_eur
        return print(f"Состояние счета: {eur_val} {Account.SUFFIX_EUR}")

    def add_percent(self):
        self.__value += self.__value * self.__percent
        print("Проценты были успешно начислены")
        self.balance()

    def add_money(self, val):
        self.verify_value(val)
        self.__value += val
        print(f"{val} {Account.SUFFIX} было успешно добавлено!")
        self.balance()

    def withdraw_money(self, val):
        self.verify_value(val)
        if val > self.__value:
            print(f"К сожалению у вас нет {val} {Account.SUFFIX}")
        else:
            self.__value -= val
            print(f"{val} {Account.SUFFIX} было успешно снято!")
        self.balance()

    @staticmethod
    def verify_surname(surname):
        if not isinstance(surname, str):
            raise TypeError("Фамилия должна быть строкой")
        st = re.findall(r'[^a-zа-яё]', surname, re.IGNORECASE)
        if st:
            raise TypeError("В строке должны быть только буквы")

    @staticmethod
    def verify_num(num):
        if not isinstance(num, str):
            raise TypeError("Номер должна быть строкой")
        st = re.findall(r'[^0-9]', num, re.IGNORECASE)
        if st:
            raise TypeError("В строке должны быть только цифры")

    @staticmethod
    def verify_percent(percent):
        if not isinstance(percent, (int, float)):
            raise TypeError("Проценты должна быть цифрой")
        if not 0 <= percent <= 0.2:
            raise TypeError("Проценты не должны быть меньше ноля, и больше 20")

    @staticmethod
    def verify_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Номер должна быть цифрой")
        if value < 0:
            raise TypeError("Сумма не может быть отрицательной")

    def print_info(self):
        print("Информация о счете")
        print('-' * 20)
        print(f'#{self.__num}')
        print(f'Владелец: {self.__surname}')
        self.balance()
        print(f'Проценты: {self.__percent:.1%}')
        print('-' * 20)


acc = Account('Кард', '12345', 0.028, 1000)
acc.print_info()
acc.balance()
acc.get_convert_to_usd()
acc.get_convert_to_eur()
print()
Account.rate_usd = 2
Account.rate_eur = 3
acc.get_convert_to_usd()
acc.get_convert_to_eur()
print()

acc.set_surname('Замшина')
acc.print_info()
acc.add_percent()
print()

acc.withdraw_money(1000)
print()

acc.withdraw_money(3000)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)
print()


class AccountTwo:
    rate_usd = 0.013
    rate_eur = 0.011
    SUFFIX = 'RUB'
    SUFFIX_USD = 'USD'
    SUFFIX_EUR = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.verify_surname(surname)
        self.verify_num(num)
        self.verify_percent(percent)

        self.__surname = surname
        self.__num = num
        self.__percent = percent
        self.__value = value
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт")
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт")

    @property
    def change_surname(self):
        return self.__surname

    @change_surname.setter
    def change_surname(self, surname):
        self.verify_surname(surname)
        self.__surname = surname

    @property
    def change_num(self):
        return self.__num

    @change_num.setter
    def change_num(self, num):
        self.verify_num(num)
        self.__num = num

    @property
    def change_percent(self):
        return self.__percent

    @change_percent.setter
    def change_percent(self, percent):
        self.verify_percent(percent)
        self.__percent = percent

    @property
    def change_value(self):
        return self.__value

    @change_value.setter
    def change_value(self, value):
        self.verify_value(value)
        self.__value = value

    @property
    def balance(self):
        return f"Баланс счета: {self.__value} {self.SUFFIX}"

    @property
    def convert_to_usd(self):
        usd_val = self.__value * AccountTwo.rate_usd
        return f"Состояние счета: {usd_val} {AccountTwo.SUFFIX_USD}"

    @property
    def convert_to_eur(self):
        eur_val = self.__value * AccountTwo.rate_eur
        return f"Состояние счета: {eur_val} {AccountTwo.SUFFIX_EUR}"

    @property
    def add_percent(self):
        self.__value += self.__value * self.__percent
        return f"Проценты были успешно начислены \n{self.balance}"

    @property
    def add_money(self):
        return

    @add_money.setter
    def add_money(self, val):
        self.verify_value(val)
        self.__value += val
        print(f"{val} {AccountTwo.SUFFIX} было успешно добавлено! \n{self.balance}")

    @property
    def withdraw_money(self):
        return

    @withdraw_money.setter
    def withdraw_money(self, val):
        self.verify_value(val)
        if val > self.__value:
            print(f"К сожалению у вас нет {val} {AccountTwo.SUFFIX} \n{self.balance}")
        else:
            self.__value -= val
            print(f"{val} {AccountTwo.SUFFIX} было успешно снято! \n{self.balance}")

    @staticmethod
    def verify_surname(surname):
        if not isinstance(surname, str):
            raise TypeError("Фамилия должна быть строкой")
        st = re.findall(r'[^a-zа-яё]', surname, re.IGNORECASE)
        if st:
            raise TypeError("В строке должны быть только буквы")

    @staticmethod
    def verify_num(num):
        if not isinstance(num, str):
            raise TypeError("Номер должна быть строкой")
        st = re.findall(r'[^0-9]', num, re.IGNORECASE)
        if st:
            raise TypeError("В строке должны быть только цифры")

    @staticmethod
    def verify_percent(percent):
        if not isinstance(percent, (int, float)):
            raise TypeError("Проценты должна быть цифрой")
        if not 0 <= percent <= 0.2:
            raise TypeError("Проценты не должны быть меньше ноля, и больше 20")

    @staticmethod
    def verify_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Номер должна быть цифрой")
        if value < 0:
            raise TypeError("Сумма не может быть отрицательной")

    def print_info(self):
        print("Информация о счете")
        print('-' * 20)
        print(f'#{self.__num}')
        print(f'Владелец: {self.__surname}')
        print(self.balance)
        print(f'Проценты: {self.__percent:.1%}')
        print('-' * 20)


acc_two = AccountTwo('Кард', '12345', 0.028, 1000)
acc_two.print_info()
print(acc_two.convert_to_usd)
print(acc_two.convert_to_eur)
print()

AccountTwo.rate_usd = 2
AccountTwo.rate_eur = 3
print(acc_two.convert_to_usd)
print(acc_two.convert_to_eur)
print()

acc_two.change_surname = 'Замшина'
acc_two.print_info()
print(acc_two.add_percent)
print()

acc_two.withdraw_money = 1000
print()

acc_two.withdraw_money = 3000
print()

acc_two.add_money = 5000
print()

acc_two.withdraw_money = 3000
