"""COFFEE MACHINE PROGRAM"""
import re


class Coffee:
    res = {'Water': '1000ml',
           'Milk': '1000ml',
           'Money': '0.00$',
           'Coffee': '1000g'}

    def __init__(self):
        print('---------------------------------------------------------------------------\n')
        print('\nWELCOME TO BESTENLIST COFFEE MACHINE\n')
        self.order = int()
        self.coins = str()
        self.q = float()
        self.d = float()
        self.n = float()
        self.s = float()
        self.total = float()
        self.orderPrice = float()
        self.money = float(re.findall('[0-9.0-9]+', self.res['Money'])[0])
        self.water = int(re.findall('[0-9]+', self.res['Water'])[0])
        self.milk = int(re.findall('[0-9]+', self.res['Milk'])[0])
        self.coffe = int(re.findall('[0-9]+', self.res['Coffee'])[0])
        try:
            self.option = input("""Enter your option:
                                        1. To Order
                                        2. Show Report
                                        3. Cancel Process\n""")
            if self.option == 'off':
                self.shutdown()
            elif int(self.option) == 1:
                self.forder()
            elif int(self.option) == 2:
                self.print()
            elif int(self.option) == 3:
                print('\nSee you again, Have a nice day!')

        except Exception:
            print('\nTry again\n')
            print('----------------------------------------------------------------------\n')
            self.__init__()

    def shutdown(self):
        return

    def print(self):
        print()
        for keys, values in self.res.items():
            print(keys, values)
        self.__init__()

    # to order
    def forder(self):
        self.order = int(input("""Enter your Order Number: 
                                    1. Espresso
                                    2. Latte
                                    3. Cappuccino\n"""))
        self.pOrder(self.order)

    # to check resource
    def cRes(self, wat, mil, cpow, order):
        if float(re.findall('[0-9]+', self.res['Water'])[0]) - wat <= 0:
            print('\nNot enough Water, Try again later')
            self.__init__()
        elif float(re.findall('[0-9]+', self.res['Milk'])[0]) - mil <= 0:
            print('\nNot enough Milk, Try again later')
            self.__init__()
        elif float(re.findall('[0-9]+', self.res['Coffee'])[0]) - cpow <= 0:
            print('\nNot enough Coffee Powder, Try again later')
            self.__init__()
        else:
            return self.pCoins(order)

    # to process coins
    def pCoins(self, order):
        if order == 1:
            print('\nYour Order price is 5.75$')
            self.orderPrice = 5.75

        elif order == 2:
            print('\nYour Order price is 2.75$')
            self.orderPrice = 2.75

        elif order == 3:
            print('\nYour Order price is 10.55$')
            self.orderPrice = 10.55

        print("""\nInsert Coins: 
                            q. quarters(0.25$)
                            d. dimes(0.10$)
                            n. nickles(0.05$)
                            p. pennies(0.01$)""")
        return self.getCoins(self.orderPrice)

    # to check transaction
    def ctrans(self, total, orderprice):
        if total > orderprice:
            print(f'Here is {round(total - orderprice, 2)} change\n')
            self.res['Money'] = f'{round(self.money + orderprice, 2)}$'
            self.makeCoffee(self.money, self.order)
        elif total < orderprice:
            print(f'sorry that is not enough, Money refunded, Try again\n')
            self.getCoins(orderprice)
        return

    # to get coins
    def getCoins(self, orderprice):
        self.coins = input()
        self.q = re.findall('[q]', self.coins).count('q') * 0.25
        self.d = re.findall('[d]', self.coins).count('d') * 0.10
        self.n = re.findall('[n]', self.coins).count('n') * 0.05
        self.s = re.findall('[s]', self.coins).count('s') * 0.01
        self.total = self.q + self.d + self.n + self.s
        return self.ctrans(self.total, orderprice)

    # to process order
    def pOrder(self, order):
        if order == 1:
            return self.cRes(150, 100, 15, order)
        elif order == 2:
            return self.cRes(200, 100, 7, order)
        elif order == 3:
            return self.cRes(50, 200, 5, order)

    # to make coffee
    def makeCoffee(self, money, order):
        if order == 1:
            self.res['Milk'] = f'{self.milk - 150}ml'
            self.res['Water'] = f'{self.water - 100}ml'
            self.res['Coffee'] = f'{self.coffe - 15}g'
            print('Hey! Here is your Order Espresso!\n')
        elif order == 2:
            self.res['Milk'] = f'{self.milk - 100}ml'
            self.res['Water'] = f'{self.water - 200}ml'
            self.res['Coffee'] = f'{self.coffe - 7}g'
            print('Hey! Here is your Order Latte!\n')
        elif order == 3:
            self.res['Milk'] = f'{self.milk - 200}ml'
            self.res['Water'] = f'{self.water - 50}ml'
            self.res['Coffee'] = f'{self.coffe - 5}g'
            print('Hey! Here is your Order cappuccino!\n')

        self.__init__()


coffee = Coffee()
