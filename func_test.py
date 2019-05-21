# print('abc', end='\n\n')
# print('abc')


# def func(a, b, c):
#     print('a = %s' % a)
#     print('b = %s' % b)
#     print('c = %s' % c)
#
#
# func(1, c=3, b=2)


# 取得参数的个数
# def howlong(first, *other):
#     print(1 + len(other))
#
#
# howlong(123, 223, 455, 4545)


# var1 = 123
#
#
# def func():
#     global var1
#     var1 = 2333
#     print(var1)
#
#
# func()
# print(var1)

# list1 = [1, 2, 3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))

# for i in range(10, 20, 2):
#     print(i)


# def frange(star, stop, step):
#     x = star
#     while x < stop:
#         yield x
#         x += step
#
#
# for i in frange(10, 20, 0.5):
#     print(i)


# lambda: True

# def add(x, y):
#     return x + y
#
#
# add(3, 8)
# a = lambda x, y: x + y
# print(a(4, 6))

# a = [1, 3, 4, 5, 6, 8]
# list(filter(lambda x: x > 2, a))

def sum(a):
    def add(b):
        return a + b

    return add


print(sum(2))