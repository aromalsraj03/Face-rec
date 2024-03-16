import cv2
import os
import pickle
import face_recognition
import numpy as np
import cvzone

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)


imgBackground = cv2.imread('Resources/background.png')
# importing the mode images into alist
folderModePath='Resources/Modes'
modepath=os.listdir(folderModePath)
imgModeList=[]
for path in modepath:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
#print(len(imgModeList))
#load theencoding file
print("loading.......")
file = open('EncodeFile.p','rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown,studentIds=encodeListKnownWithIds
 #print(studentIds)
print("loaded")
 
while True:
    ret,frame = cam.read()
    
    
    imgS=cv2.resize(frame,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
    
    
    
    faceCurFrame =face_recognition.face_locations(imgS) 
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)
    
    
    imgBackground[162:162+480,55:55+640] = frame
    imgBackground[44:44+633,808:808+414] = imgModeList[1]
    
    
    for encodeFace , faceLoc in zip(encodeCurFrame,faceCurFrame):
        matches =face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis =face_recognition.face_distance(encodeListKnown,encodeFace)
        
       # print("matches",matches)
      #  print("facedis",faceDis)
    
        matchIndex = np.argmin(faceDis)
      #  print("match index",matchIndex)
        
        
        if matches[matchIndex]:
            print("known face detected")
            print(studentIds[matchIndex])
           
        else:
            print("u are not my student")
          # y1,x2,y2,x1 = faceLoc
          # y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
          # bbox = 55+x1,162+y1,x2-x1,y2-y1
          # imgBackground = cvzone.cornerRect(imgBackground,bbox,rt=0)

   # cv2.imshow("test",frame)
    cv2.imshow("FACE  ATTENDENCE",imgBackground)
    k= cv2.waitKey(1)
    
   
    
    
    