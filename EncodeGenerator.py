import cv2
import os
import face_recognition
import pickle
import time


def encodeFace(sr_code):
    folderStudentPath= "students"
    imgStudentList= [] 
    
    if(sr_code !="*"): # encodes certain faces only
        for path in sr_code:
            imgStudentList.append(cv2.imread(os.path.join(folderStudentPath, path+".jpg")))
    else:
        StudentPathList = os.listdir(folderStudentPath)
        sr_code=[] #sr-code

        for path in StudentPathList:
            imgStudentList.append(cv2.imread(os.path.join(folderStudentPath, path)))
            sr_code.append(os.path.splitext(path)[0])
        

    # loop thru image and encode every single
    def findEncodings(imagesList):
        encodeList=[]
        for img in imagesList:
            img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #opencv is bgr but face-recognition is rgb
            encode=face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
            
            
        return encodeList
            
    encodeListKnown= findEncodings(imgStudentList)
    encodeListKnownWithIDs=[sr_code, encodeListKnown]


    # putting the face encodings with ID in pickle file
    file=open("EncodeFile.p", 'wb')
    pickle.dump(encodeListKnownWithIDs, file)
    file.close()

    return True



start_time = time.time()
encodeFace()
print("--- %s seconds ---" % (time.time() - start_time))

