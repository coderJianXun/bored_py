# user1 = {'name': 'tom', 'hp': 100}
# user1 = {'name': 'jerry', 'hp': 100}
#
#
# def print_role(rolename):
#     print('name is %s . hp is %s' % (rolename['name'], rolename['hp']))
#
#
# print_role(user1)


class Player():  # 定义一个类
    def __init__(self, name, hp, occu):
        self.__name = name  # 变量被称为属性
        self.hp = hp
        self.occu = occu

    def print_role(self):
        print('%s:  %s, %s' % (self.__name, self.hp, self.occu))

    def updateName(self, newname):
        self.__name = newname


class Monster():
    '定义怪物类'

    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print('移动到某一个位置')

    def whoani(self):
        print('我是怪物父类')


class Animals(Monster):
    '普通怪物'

    def __init__(self, hp=10):
        super().__init__(hp)


class Boss(Monster):
    'Boss类'

    def __init__(self, hp=10):
        super().__init__(hp)

    def whoani(self):
        print('我是怪物Boss类')


a1 = Monster(200)
print(a1.hp)
print(a1.run())
a2 = Animals(1)
print(a2.hp)
print(a2.run())
a3 = Boss(900)
a3.whoani()

print(type(a3))
print(type(a2))
print(type(a1))
print(isinstance(a2, Monster))
print(isinstance(a3, Monster))

# user1 = Player('tom', 100, 'war')  # 类的实例化
# user2 = Player('jerry', 90, 'master')
# user1.print_role()
# user2.print_role()
#
# user1.updateName('wilson')
# user1.print_role()
