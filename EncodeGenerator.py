import cv2
import face_recognition
import pickle
import os



# importing the students images into alist
folderPath='Images'
pathList=os.listdir(folderPath)
print(pathList)
imgList=[]
StudentIds=[]
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
   
    StudentIds.append(os.path.splitext(path)[0])
    print(path)
 #   print(os.path.splitext(path)[0])
print(StudentIds)



def findEncodings(imagesList):
    encodeList=[]
    for img in imagesList:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
        
        
    return  encodeList
print("encodig started......")
encodeListKnown = findEncodings(imgList) 
encodeListKnownWithIds=[encodeListKnown,StudentIds]
print("encoding complete") 

file = open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("file saved")