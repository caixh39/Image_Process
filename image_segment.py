#coding=utf-8
#
# 测试需要，裁剪图片，使用之前学过的技术
# 做一个裁剪的小案例

import os
import pylab as plb
import PIL.Image as Image

# #读取path路径下的 jpg文件
# def getAllImages(path):
#     #f.endswith（）  限制文件类型
#     #f.endswith('.jpg')|f.endswith('.png')  改成这句可以读取jpg/png格式的文件
#     #注意 返回的是绝对路径
#    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]


# #循环读图
# for path in getAllImages('/home/cuhksz/Videos/emotion/happy'):
#     #读图
#     img = Image.open(path)
#     #cropImg = img[600:1200,750:1500] 
#     #显示
#     plb.imshow(img)
#     #设置裁剪点（4个）
#     corner = plb.ginput(4)

#     #顺时针取点求解
#     left = (corner[0][0] + corner[3][0])/2
#     top = (corner[1][1] + corner[0][1])/2
#     reight = (corner[1][0] + corner[2][0])/2
#     under = (corner[3][1] + corner[2][1])/2

#     print left,top,reight,under
#     #box = [left,top,reight,under]
#     #box中的数必须是 int 否则会报错
#     box = [int(left),int(top),int(reight),int(under)]
#     #裁剪
#     img2 = img.crop(box)
#     #显示裁剪后的效果
#     #plb.imshow(img2)
#     #plb.show()
#     #储存为原来路径覆盖原文件
#     img2.save(path)
# plb.show()

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
