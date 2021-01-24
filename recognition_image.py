import matplotlib.pyplot as plt
import cv2

file_path = '../../../Downloads/test_image/cat1.jpg'
img = cv2.imread(file_path)

## 이미지 tensor 표현값으로 가져옴
# print(img)

## 전체적인 이미지의 세로, 가로 픽셀 크기와 몇 차원 이미지인지 출력
# print('image shape: ', img.shape)

## img[n][m]의 RGB 값 출력
print(img[4][10])