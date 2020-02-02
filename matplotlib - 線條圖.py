import numpy as aa
import matplotlib.pyplot as bb
x = aa.arange(0, 360)
y = aa.sin( x * aa.pi / 180.0 )
bb.plot(x, y)
bb.xlim(0, 720)
bb.ylim(-2.2, 2.2)
bb.title("SIN funtion 圖表")
bb.show