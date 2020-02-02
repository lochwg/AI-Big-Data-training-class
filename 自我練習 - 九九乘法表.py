
#自我練習-2
#九九乘法表
for a in range(1, 10):
    for b in range(1, 10):
        c = a * b
        print(('%d * %d = %d') % (a, b, c))
        #.fomat格式
        msg = '{0} * {1} = {2} '.format(a, b, c)
        print(msg)