from abc import ABC, abstractmethod


class AbstractOrder(ABC):

    def process_order(self):
        self.prepare_cart()
        self.make_payment()
        self.ship_order()

    @abstractmethod
    def prepare_cart(self): pass

    @abstractmethod
    def make_payment(self): pass

    @abstractmethod
    def ship_order(self): pass


class Order(AbstractOrder):

    def prepare_cart(self):
        print("Preparing cart...")

    def make_payment(self):
        print("Making payment...")

    def ship_order(self):
        print("Shipping order...")


order = Order()
order.process_order()


