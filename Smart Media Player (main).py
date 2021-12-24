#!/usr/bin/env python
# coding: utf-8

# In[1]:


def facedetect():
    import cv2
    import sys
    import logging as log
    import datetime as dt
    from time import sleep

    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    log.basicConfig(filename='webcam.log',level=log.INFO)

    video_capture = cv2.VideoCapture(0)
    anterior = 0

    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass

        #Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        if anterior != len(faces):
            anterior = len(faces)
            log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))
            
        return len(faces) #returning length of the list 'faces' which constitutes number of face detected

    #When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()


# In[3]:


import vlc
import keyboard
face = facedetect()
my_Media = vlc.MediaPlayer("C:\\Users\\HP\\Downloads\\Venom Let There Be Carnage (2021) [720p] [WEBRip] [YTS.MX]\\Venom.Let.There.Be.Carnage.2021.720p.WEBRip.x264.AAC-[YTS.MX].mp4")
if(face==0):
    print("No Face Detected.")
else:
    my_Media.play()
x = 0
flag = my_Media.is_playing()
while(flag==0 or flag):
    face = facedetect()
    flag = my_Media.is_playing()
    if keyboard.is_pressed('q'):  #if key 'q' is pressed to quit the player
        break
    elif(x==5): #maximum wait limit after the face is not detected
        break
    elif(face and flag==0): #case in which face is detected but the player state is paused
        my_Media.play()
        x = 0
    elif(face==0 and flag): #case in which no face is detected but the player state is play
        my_Media.pause()
    elif(face==0 and flag==0): #case in which no face is detected and player state is pause then we just increment the waiting variable
        x+=1
        print("Face Not detected:",x)
my_Media.stop()

