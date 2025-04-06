class Circle:
    def __init__(self, r):
        self.r = r
    def get_area(self):
        return self.r *self.r * 3.14
    def get_perimeter(self):
        return 2 * self.r * 3.14

x=eval(input('请输入圆的半径:'))
r=Circle(x)
print('圆的面积为:',r.get_area())
print('圆的周长为:',r.get_perimeter())