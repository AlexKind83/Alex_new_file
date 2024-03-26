class DescriptorOrder:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Сумма и количество должно быть числом!")
        if value < 0:
            raise ValueError("Цена и количество товара не может быть отрицательным")
        instance.__dict__[self.__name] = value


class Order:
    price = DescriptorOrder()
    quantity = DescriptorOrder()

    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity


order = Order('iPhone 14 Pro Max', 104_000, 10)

order.price = 102_000
order.quantity = 8
print(f"Цена: {order.price} \nКоличество: {order.quantity}")
print(order.__dict__)

