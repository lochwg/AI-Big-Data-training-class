import cv2
from matplotlib import pyplot as plt
img_bgr = cv2.imread('Nikola_Tesla.jpg')
img_gray = cv2.imread('Nikola_Tesla.jpg', cv2.IMREAD_GRAYSCALE)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# =============================================================================
# 原始 OpenCV 是使用 'BGR'
# =============================================================================
#使用 matplotlib 顯示圖片
plt.figure()
plt.subplot(1,2,1)
plt.axis('off')  # 不顯示座標
plt.imshow(img_gray, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(img_rgb)
plt.show()