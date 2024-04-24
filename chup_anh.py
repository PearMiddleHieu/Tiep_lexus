from picamera import PiCamera
import time
#import cv2
camera = PiCamera()
time.sleep(2)
camera.capture("/home/pi/Desktop/STOP_11.jpg")
#cv2.imshow(camera)
print("Done.")