import cv2
img = cv2.imread('OTTER_2.jpg')
#以灰階的方式讀取圖檔
img_gray = cv2.imread('OTTER_2.jpg', cv2.IMREAD_GRAYSCALE)
#可以讓視窗自由縮放大小
cv2.namedWindow('Cuite Otter', cv2.WINDOW_NORMAL)

cv2.imshow('Cuite Otter', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
