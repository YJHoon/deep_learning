import matplotlib.pyplot as plt
import cv2

file_path = '../../../Downloads/test_image/cat1.jpg'
img = cv2.imread(file_path)

## 이미지 tensor 표현값으로 가져옴
# print(img)

## 전체적인 이미지의 세로, 가로 픽셀 크기와 몇 차원 이미지인지 출력
# print('image shape: ', img.shape)

## img[n][m]의 RGB 값 출력
# print(img[4][10])



##################### rgb값으로 스크린에 점 찍기 ########################
## pygame => 파이썬을 통해 게임 개발 가능하게 해주는 모듈
# import pygame
# WHITE = (255, 255, 255)
# (width, height) = (200, 300)
# running = True

# def main():
#     global running, screen
#     pygame.init() # pygame 초기화 
#     screen = pygame.display.set_mode((width, height)) # 창 크기 설정
#     pygame.display.set_caption("TUFF") # 창 이름 설정
#     screen.fill(WHITE) # 백그라운드 색 설정
#     pygame.display.update() # 설정값 업데이트

#     while running:
#       ev = pygame.event.get()
#       for event in ev:
#           if event.type == pygame.MOUSEBUTTONUP: # 마우스 클릭이 끝나면
#               drawCircle() # 좌표값을 받아와 원을 그림
#               pygame.display.update() # 그걸 업데이트 해줌 (업데이트 안 해주면 디스플레이에 반영 안 됨) 
#           if event.type == pygame.QUIT:
#               running = False

# def getPos():
#     pos = pygame.mouse.get_pos() # 마우스 위치 좌표를 받아옴
#     return (pos)


# def drawCircle():
#     pos = getPos() # getPos 함수를 통해 마우스의 좌표를 받아옴
#     pygame.draw.circle(screen, img[4][10], pos, 20) # 스크린에 이미지[4][10]의 rgb 값으로 크기 20인 원을 그림

# if __name__ == '__main__': # main 함수를 메인함수로 선언
#     main()



##################### plt 모듈을 이용한 차트. 이미지의 vector 그래프 표시 ########################
plt.imshow(img)
plt.show()
