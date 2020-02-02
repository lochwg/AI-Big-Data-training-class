import cv2
from matplotlib import pyplot as plt
img_bgr = cv2.imread('Nikola_Tesla.jpg')
img_gray = cv2.imread('Nikola_Tesla.jpg', cv2.IMREAD_GRAYSCALE)
# 數字越大 越模糊
img_gauss = cv2.GaussianBlur(img_bgr, (3, 3), 0)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

plt.figure()
# =============================================================================
# 2,2,1 代表切分為表格 2X2 第1格位置
# =============================================================================
plt.subplot(2,2,1)
plt.axis('off')
plt.imshow(img_gray, cmap='gray')

plt.subplot(2,2,2)
plt.imshow(img_rgb)

plt.subplot(2,2,3)
plt.imshow(img_gauss)

plt.show()