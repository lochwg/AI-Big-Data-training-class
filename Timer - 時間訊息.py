from threading import Timer
def print_name(str):
    print ('你好 %s' % str)
print ('Start')
Timer(5, print_name,('這是5秒出現的訊息')).start()
Timer(10, print_name,('這是10秒出現的訊息')).start()
print ('End')
