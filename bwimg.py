import cv2

ori = cv2.imread("FT(-)JH21472 A5.tif")
hasil = cv2.imread("hasil.jpg", cv2.IMREAD_UNCHANGED)

grayImage = cv2.cvtColor(ori, cv2.COLOR_BGR2GRAY)
  
#(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 170, 255, cv2.THRESH_BINARY)
print(hasil.shape)
#print(blackAndWhiteImage.shape)
print(hasil)
print(ori.shape)
#cv2.imwrite("hasil.jpg",grayImage)
#cv2.imshow("image",blackAndWhiteImage)
#cv2.waitKey(1)