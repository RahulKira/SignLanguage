import cv2
import time
import os
import time
import uuid
images_path='RealTimeObjectDetection-main/Tensorflow/workspace/images/collectedimages'
labels=['Hello','Thanks','Please','yes','no','sorry','Bye']
number_imgs=15
for label in labels:
    !mkdir {'RealTimeObjectDetection-main\Tensorflow\workspace\images\collectedimages\\'+label}
    cap=cv2.VideoCapture(0)
    print('Collecting Images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret,frame=cap.read()
        imagename=os.path.join(images_path,label+'.'+'{}.jpg'.formate(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(2)
        if cv2.waitKey(1) and 0xFF==ord('q'):
            break
    cap.release()
