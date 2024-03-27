import cv2
import os
import face_recognition
import pickle

# importing face student images into a list
folderStudentPath= "students"
StudentPathList = os.listdir(folderStudentPath)
imgStudentList= []
studentIDs=[]

for path in StudentPathList:
    imgStudentList.append(cv2.imread(os.path.join(folderStudentPath, path)))
    studentIDs.append(os.path.splitext(path)[0])
    


# loop thru image and encode every single
def findEncodings(imagesList):
    encodeList=[]
    for img in imagesList:
        img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #opencv is bgr but face-recognition is rgb
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
        
        
    return encodeList
        

print("start")
encodeListKnown= findEncodings(imgStudentList)
encodeListKnownWithIDs=[studentIDs, encodeListKnown]


# putting the face encodings with ID in pickle file
file=open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIDs, file)
file.close()
print("complete")