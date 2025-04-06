class Car:
    def __init__(self, model, number):
        self.model = model
        self.number = number
    def start(self):
        pass
    def stop(self):
        pass

class TaxiCar(Car):
    def __init__(self, model, number, owner_gs):
        Car.__init__(self, model, number)
        self.owner_gs = owner_gs
    def start(self):
        #Car.start(self)
        print(f'乘客您好！\n我是{self.owner_gs}的，我的车牌是{self.number},您要去哪里？')
    def stop(self):
        #Car.stop(self)
        print('目的地到了，请您付款下车，欢迎下次乘坐')

class FamilyCar(Car):
    def __init__(self, model, number, owner_gr):
        Car.__init__(self, model, number,)
        self.owner_gr = owner_gr
    def start(self):
        #Car.start(self)
        print(f'我是{self.owner_gr},我的汽车我做主')

    def stop(self):
        #Car.stop(self)
        print('目的地到了，我们去玩儿吧')

car1=TaxiCar('大众','苏A98876','南京客运公司')
car1.start()
car1.stop()
print('-'*40)
car2=FamilyCar('特斯拉','苏A98234','张三')
car2.start()
car2.stop()
