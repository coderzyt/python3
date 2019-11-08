class customer(object):
    buy_dict = {}

    def buy(self, pro_name, price):
        self.buy_dict[pro_name] = price


class testA(object):
    def __init__(self):
        print("created")

    def __del__(self):
        print("deleted")

    value = 0

    def printf(self):
        print(self)
        print(self.value)


class testB(object):
    def printf(self):
        self.value = 0
        print(self.value)

class vipcust(object):
    def _disct(self, prod_name, price):
        if prod_name=='apple':
            return price*0.9
        elif prod_name=='peach':
            return price*0.8
        elif prod_name=='banana':
            return price*0.7
        else:
            return price

    def buy_some(self, prod_name, price):
        disct_price = self._disct(prod_name, price)
        self.prod_dict[prod_name]=disct_price
    


if __name__ == '__main__':
    a = testA()
    a.printf()
