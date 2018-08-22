""" crop image's special zoom """

import os
import cv2

start_pos=[0,0]
select_done=False
def get_roi(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        global start_pos
        start_pos = [x,y]
        global select_done
        select_done = True
path='/home/cuhksz/Videos/emotion/fear'
path_save='/home/cuhksz/Videos/emotion/fear1'
start_cnt = 1
cv2.namedWindow('source')
cv2.setMouseCallback('source',get_roi)
for i in range(start_cnt,len(os.listdir(path))):
    select_done=False
    img = cv2.imread(path+'/fear_'+str(i)+'.jpg')
    if img is None:
        continue
    print(path+'/fear_'+str(i)+'.jpg')
    while True:
        cv2.imshow('source',img)
        if select_done is True:
            roi = img[start_pos[1]-240:start_pos[1]+240,start_pos[0]-235:start_pos[0]+235]
            cv2.imwrite(path_save+'/fear_'+str(i)+'.jpg',roi)
            break
        if cv2.waitKey(5)!=255:
            os._exit(0)
