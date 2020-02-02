import cv2, subprocess
img = cv2.imread('Bank.jpg')
cv2.namedWindow('Image')
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyWindow('Image')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
for i in range(len(inv)):
    for j in range(len(inv[i])):
        if inv[i][j] == 255:
            count = 0
            for k in range(-2, 3):
                for l in range(-2, 3):
                    try:
                        if inv[i + k][j + l] == 255:
                            count +=1
                    except IndexError:
                        pass
            if count <=6:
                inv[i][j] = 0
dilation = cv2.dilate(inv, (8,8), iterations = 1)
cv2.imwrite('', dilation)
child = subprocess.Popen('tesseract media\\bank_t.jpg result')
child.wait()
text = open('result.txt').read().strip()
print('驗證碼' + text)