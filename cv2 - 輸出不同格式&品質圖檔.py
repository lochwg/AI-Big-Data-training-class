import cv2
img = cv2.imread('OTTER_3.jpg')
img_gray = cv2.imread('OTTER_3.jpg', cv2.IMREAD_GRAYSCALE)

# =============================================================================
# 輸出圖檔 不同圖檔格式
# =============================================================================
cv2.imwrite('4.OUTTER_3_test.jpg', img_gray)
cv2.imwrite('4.OUTTER_PNG.png', img_gray)
cv2.imwrite('4.OUTTER_TIFF.tiff', img_gray)


# =============================================================================
# 輸出圖檔 不同圖片品質
# =============================================================================
# 輸出圖檔 設定JPEG圖片品質為90 (可用值為 0 ~ 100)
cv2.imwrite('4.OUTTER_test.jpg', img_gray, [cv2.IMWRITE_JPEG_QUALITY, 90])
# 輸出圖檔 設定PNG圖片品質為5 (可用值為 0 ~ 9)
cv2.imwrite('4.OUTTER_test.png', img_gray, [cv2.IMWRITE_PNG_COMPRESSION, 5])