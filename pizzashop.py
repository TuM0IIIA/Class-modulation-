"""Опять-таки это по большей части игрушечная эмуляция, но объекты и взаимодействия
 отражают работу составных объектов. В качестве эмпирического правила запомните:
 классы могут представлять почти любые объекты и отношения, которые удастся
выразить с помощью предложения; просто замените имена существительные классами
(скажем, Oven), а глаголы методами (например, bake),
 и вы получите первое приближение к проектному решению."""

from employees import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, "orders from ", server)  # orders from

    def pay(self, server):
        print(self.name, "pay for item to ", server)  # paid per unit

class Oven:
    def bake(self):
        print("oven bakes")  # oven bakes

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')  # include other obj
        self.chef = PizzaRobot('Bob')  # robot named Bob
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)  # activate another obj
        customer.order(self.server)  # orders of clients, taken by waiter
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == "__main__":
    scene = PizzaShop()  # make the composite
    scene.order("Homer")  # simulate Homer's order
    print('. . . ')
    scene.order("Shaggy")  # simulate Shaggy's order
