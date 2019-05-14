# 异常处理

# try:
#     year = int(input('input year:'))
# except (ValueError, AttributeError, KeyError):
#     print('年份要输入数字')


# try:
#     print(1 / 0)
# except Exception as e:
#     print('0不能做除数 %s' % e)


try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()