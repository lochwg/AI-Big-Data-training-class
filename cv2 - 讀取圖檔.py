# =============================================================================
# matplotlib是python的繪圖工具，接下來以matplotlib顯示OpenCV圖片 
# =============================================================================
import cv2
from matplotlib import pyplot as plt

# 使用OpenCV讀取圖檔
img_bgr = cv2.imread('Nikola_Tesla.jpg')
# 將BGR圖片轉為RGB圖片
img_rgb = img_bgr[:,:,::-1]
# =============================================================================
# 測試
# img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# =============================================================================

plt.imshow(img_rgb)
plt.show()