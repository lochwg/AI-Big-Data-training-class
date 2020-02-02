import cv2, numpy
cv2.namedWindow('plot')
image = cv2.imread('Nikola_Tesla.jpg')
cv2.line(image, (50,50), (300,300), (255,0,0), 2)
cv2.rectangle(image, (500,20), (580,100), (0,255,0), 3) #方形
cv2.rectangle(image, (100,300), (150,360), (0,0,255), -1) #方形填滿
cv2.circle(image, (500,300), 40, (255,255,0), -1)
pts = numpy.array([[300,300], [300,340], [350,320]], numpy.int32)

cv2.polylines(image, [pts], True, (0, 255, 255), 2) #三角形
cv2.putText(image, 'output', (), cv2.FONT_HERSHEY_SIMPLEX, 1 (255,255,255), 2)
cv2.imshow('plot', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
