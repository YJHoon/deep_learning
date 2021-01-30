import matplotlib.pyplot as plt
import cv2
import os

input_dir = '/Users/jehoon/Downloads/test_image'
files = os.listdir(input_dir)


## 해당 directory에 있는 파일 개수와 이름 출력
print('The number of files : ', len(files))
print('File names in the directory : ')
cnt = 0
for file in files:
  cnt += 1
  print('{0}. {1}'.format(cnt, file)) # 파이썬 print format



## 전체 경로 return
import glob # 인자로 받은 패턴과 이름이 일치하는 리스트들을 반환

input_dir = '/Users/jehoon/Downloads/test_image/*'
files = glob.glob(input_dir) # 해당 디렉토리에 있는 모든 파일과 디렉토리를 반환 한다 -> 인자로 * 을 넘겨줘서
print('The number of files : ', len(files))
print('File names in the directory : ')
for file in files:
  print(file)


## f string 이용
#import glob

dir_choice = 'test_image'
input_dir = f'/Users/jehoon/Downloads/{dir_choice}/*'
files = glob.glob(input_dir)

for file in files:
  print(file)