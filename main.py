import cv2
import os
import pickle
import face_recognition

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground= cv2.imread("Resources/background.png")
# importing mode images into a list
folderModePath= "resources/Modes"
modePathList = os.listdir(folderModePath)
imgModeList= []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# load encodefile
file= open("EncodeFile.p", 'rb')
encodeListKnownWithIDs= pickle.load(file)
file.close()
studentIDs, encodeListKnown= encodeListKnownWithIDs


print(studentIDs)
while True:
    success, img= cap.read()
    
    imgSmall= cv2.resize(img, (0,0), None, 0.25, 0.25) #make the video smaller, for small computational power
    imgSmall= cv2.cvtColor(imgSmall,cv2.COLOR_BGR2RGB)
    
    faceCurrFrame= face_recognition.face_locations(imgSmall) #looks for the face
    encodeCurrFrame= face_recognition.face_encodings(imgSmall, faceCurrFrame) #matches the current face with the encodings, not the whole image
    
    
    imgBackground[162:162+480, 55:55+640]= img
    imgBackground[44:44+633, 808:808+414]=imgModeList[0]
    
    for encodeFace, faceLoc in zip(encodeCurrFrame, faceCurrFrame):
        matches=face_recognition.compare_faces(encodeListKnown, encodeFace)
        matches=face_recognition.compare_faces(encodeListKnown, encodeFace) #lower distance, better match
        faceDistance=face_recognition.face_distance(encodeListKnown, encodeFace)
        print("Matches: ", matches)
        print("Face distance: ", faceDistance)
    
    cv2.imshow("Face attendance", imgBackground) 
    cv2.waitKey(1)
    