import cv2
import numpy as np
import time

def diffImg(t0, t1, t2):  #function that takes in 3 images and detects what is moving within the images returns a single images that only shows what objects have moved

  d1 = cv2.absdiff(t2, t1) #subtracts each image from each other

  d2 = cv2.absdiff(t1, t0) #subtracts each image from each other
  final = cv2.bitwise_and(d1, d2)
  '''
  smallX = (int)(final.shape[1]/10-400)
  bigX = (int)(final.shape[1]/10+200)
  smallY = (int)(final.shape[0]/10-150)
  bigY = (int)(final.shape[0]/10+150)
  cv2.rectangle(final,(smallX, smallY), (bigX, bigY),(255,255,255),5)
  '''
  return final #returns the final image

cam = cv2.VideoCapture(0)

print (cam.isOpened())

winName = "Movement Indicator"

cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

# Read three images first:

lol, img = cam.read()

t_minus = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

t = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

t_plus = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)



while True:
  send = diffImg(t_minus, t, t_plus)
  cv2.imshow( winName, send)
  #img = cv2.imshow( winName, diffImg(t_minus, t, t_plus))
  # Read next image

  useless, thresh = cv2.threshold(send,25,255,cv2.THRESH_BINARY)
  #threshhsv = cv2.cvtColor(thresh, cv2.COLOR_BGR2HSV)
  #can = cv2.Canny(thresh)
  winName2 = "Thresh"
  im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  cv2.drawContours(thresh, contours, -1, (255,0,255), 1)
  '''
  sum1 = 0
  sum2 = 0
  count = 0
  if len(contours) != 0:
    for j in contours:
      for i in j:
        sum1+=i[0][0]
        sum2+=i[0][1]
        count += 1
    sum1/count
    sum2/count
    print "x: %s" % sum1
    print "y: %s" % sum2
  '''
  cv2.imshow(winName2, thresh)
  t_minus = t
  t = t_plus
  t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
  key = cv2.waitKey(10) #if escape key is pressed exit program for testing only

  
  if key == 27:
    cv2.destroyWindow(winName)
    cv2.destroyWindow(winName2)
    break
