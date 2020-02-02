import cv2
img_bgr = cv2.imread('Nikola_Tesla.jpg')

img_gauss = cv2.GaussianBlur(img_bgr, (7, 7), 100)
cv2.imwrite('8.Gauss.jpg', img_gauss)

img_gray = cv2.cvtColor(img_gauss, cv2.COLOR_RGB2GRAY)
cv2.imwrite('8.gray.jpg', img_gray)

ret, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite('8.binary.jpg', img_binary)
