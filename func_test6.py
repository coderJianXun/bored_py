# fd = open('name.txt')
# try:
#     for line in fd:
#         print(line)
# finally:
#     fd.close()

# 匿名函数 lambda
# 闭包 func

with open('name.txt') as f:
    for line in f:
        print(line)
