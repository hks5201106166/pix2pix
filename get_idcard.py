import cv2
import os
path='/home/ubuntu/hks/ocr/pix2pix/datasets/remove_logo_and_aug_image2/train/'
files=os.listdir(path)
for file in files:
    image=cv2.imread(os.path.join(path+file))
    h,w,c=image.shape
    image=image[:,0:int(w/2),:]
    cv2.imwrite('/home/ubuntu/hks/ocr/pix2pix/datasets/remove_logo_and_aug_image4/train/'+file,image)