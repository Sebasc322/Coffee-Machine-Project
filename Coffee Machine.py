print("Welcome to the Coffee Machine!")


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.action = None
        self.buy_input = None

    def input_action(self):
        print('What would you like to do? (buy, fill, take, remaining, exit):')
        self.action = input()
        if self.action == 'exit':
            print("Thank you. Now closing.")
        elif self.action == 'buy':
            self.buy_action()
        elif self.action == 'fill':
            self.fill_action()
        elif self.action == 'take':
            self.take_action()
        elif self.action == 'remaining':
            self.remaining_action()
        else:
            self.input_action()

    def buy_action(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        self.buy_input = input()
        if self.buy_input == '1':
            if self.water < 250:
                print('Sorry, not enough water!')
            elif self.beans < 16:
                print('Sorry, not enough beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
                print('I have enough resources, making you a coffee!')
            self.input_action()
        elif self.buy_input == '2':
            if self.water < 350:
                print('Sorry, not enough water!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.beans < 20:
                print('Sorry, not enough beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
                print('I have enough resources, making you a coffee!')
            self.input_action()
        elif self.buy_input == '3':
            if self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.beans < 12:
                print('Sorry, not enough beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
                print('I have enough resources, making you a coffee!')
            self.input_action()
        elif self.buy_input:
            self.input_action()
        else:
            self.input_action()

    def fill_action(self):
        self.fill_water()
        self.fill_milk()
        self.fill_beans()
        self.fill_cups()
        self.input_action()

    def fill_water(self):
        print('How many ml of water do you want to add:')
        add_water = int(input())
        self.water += add_water

    def fill_milk(self):
        print('Write how many ml of milk do you want to add:')
        add_milk = int(input())
        self.milk += add_milk

    def fill_beans(self):
        print('Write how many grams of coffee beans do you want to add:')
        add_beans = int(input())
        self.beans += add_beans

    def fill_cups(self):
        print('Write how many disposable cups of coffee do you want to add:')
        add_cups = int(input())
        self.cups += add_cups

    def take_action(self):
        print('I gave you ' + str(self.money))
        self.money -= self.money
        self.input_action()

    def remaining_action(self):
        print("The coffee machine has:")
        print(str(self.water) + ' of water')
        print(str(self.milk) + ' of milk')
        print(str(self.beans) + ' of coffee beans')
        print(str(self.cups) + ' of disposable cups')
        print(str(self.money) + ' of money')
        self.input_action()


coffee_machine_1 = CoffeeMachine()
coffee_machine_1.input_action()
