#coding=utf-8 

import cv2
import sys
import os.path
import shutil

def detect(filename, cascade_file = "lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread("/Users/sakurakouji/Desktop/tmp/pics/"+filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = cascade.detectMultiScale(gray,
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (24, 24))

 #   if faces.all():
 #       print("noooooooooo!")
    for (x, y, w, h) in faces:
        #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cropimg=image[y:y+h,x:x+w]
    try:
        cv2.imwrite("faces/"+filename, cropimg)
    except UnboundLocalError:
        shutil.copyfile("/Users/sakurakouji/Desktop/tmp/pics/"+filename,"/Users/sakurakouji/Desktop/tmp/not_detected/"+filename)
    
#    cv2.imshow("AnimeFaceDetect", cropimg)
#    cv2.waitKey(0)
   
path='/Users/sakurakouji/Desktop/tmp/pics';
filelist=os.listdir(path)
#print filelist
for files in filelist:
    print "正在对"+files+"进行操作"
    detect(files)

print "已完成所有操作"
