
def one(a, *b):
#a是一個普通傳入參數，*b是一個非關鍵字星號參數
    print(b)
one (1,2,3,4,5,6)

def two(a=1,**b):
    print(b)
#a是一個普通關鍵字參數，**b是一個關鍵字雙星號參數
two (a=1, b=2, c=3, d=4, e=5, f=6)