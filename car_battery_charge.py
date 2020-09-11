# NEW！为子类添加新的属性和方法
class Car():
    def __init__(self, year, brand, type):
        self.year = year
        self.brand = brand
        self.type = type
        self.mile = 1000
        self.petro = 80

    def car_name(self):
        car_name = 'My car is ' + str(self.year) + ' ' + self.brand + ' ' + self.type + '.'
        return car_name

    def update_mile(self, mile_reading):
        self.mile += mile_reading

    def car_miles(self):
        car_miles = "The car's updated miles are " + str(self.mile) + 'km.'
        return car_miles

    def fill_petro(self, petro_reading):
        if petro_reading < self.petro:
            petro_reading = self.petro
            print('需要加油！')
        else:
            print('暂时不需要加油！')


class Battery():
    def __init__(self, battery_original_volume=5000):
        self.battery_original_volume = battery_original_volume

    def used_battery(self, reading_volume):
        if reading_volume < self.battery_original_volume:
            print('需要换电池!')
        else:
            print("电池条件良好!")


class Charge():
    def __init__(self, safe_battery_percentage=0.3):
        self.safe_battery_percentage = safe_battery_percentage

    def battery_reading(self, reading_percentage):
        if self.safe_battery_percentage < reading_percentage:
            self.safe_battery_percentage = reading_percentage
            print('电量' + str(reading_percentage * 100) + '%充足！可以行驶！')
        else:
            print('电量过低，请充电！')


class Electric_car(Car):
    def __init__(self, year, brand, type):
        # super() 是一个特殊函数，帮助Python将父类和子类关联起来，调用Electric_car 的父类的方法__init__()
        super().__init__(year, brand, type)
        self.battery = Battery()
        self.charge = Charge()

    # 对父类没用的方法，如果调用则剔除！
    def fill_petro(self):
        print('电车不需要加油！')


# 注意写法！
my_e_car = Electric_car(2020, 'BYD', '秦')
my_e_car.update_mile(1000)
print(my_e_car.car_name() + '\n' + my_e_car.car_miles())

# 注意写法！
my_e_car.battery.used_battery(6000)
my_e_car.charge.battery_reading(0.4)
my_e_car.fill_petro()

print('\n')
