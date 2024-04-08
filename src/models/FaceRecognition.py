import cv2
import math
import face_recognition
import numpy as np
import cvzone

import models, utils

class FaceRecognition:
    student_IDs=[]
    encodeListKnown=[]
    
    def __init__(self):
        self.student_IDs, self.encodeListKnown= utils.Utilities.readFaceEncodings()
        self.realtimeRecognition()
        
    def face_confidence(face_distance, face_match_threshold=0.6): # computes confidence percent, has bug, idk why
        range= (1.0 - face_match_threshold)
        linear_val= (1.0-face_distance) / (range * 2.0)
        
        if (face_distance > face_match_threshold):
            return str(round(linear_val * 100, 2)) + '%'
        else:
            value= (linear_val+((1.0-linear_val)* math.pow((linear_val - 0.5) *2, 0.2))) * 100
            return str(round(value, 2)) + '%'
    def realtimeRecognition(self): # realtime face recognition from cv video capture, must be inside pyqt component
        imgBackground= cv2.imread("Resources/background.png")
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)
        while True:
            ret, img= cap.read()
            
            imgSmall= cv2.resize(img, (0,0), None, 0.25, 0.25) # make the video smaller, for small computational power
            imgSmall= cv2.cvtColor(imgSmall,cv2.COLOR_BGR2RGB)
            
            faceCurrFrame= face_recognition.face_locations(imgSmall) # looks for the face
            encodeCurrFrame= face_recognition.face_encodings(imgSmall, faceCurrFrame) # matches the current face with the encodings, not the whole image
            imgBackground[162:162+480, 55:55+640]= img
            
            confident=False
            almost_confident=False
            for encodeFace, faceLoc in zip(encodeCurrFrame, faceCurrFrame):
                if(confident or almost_confident):
                    pass
                else:
                    matches=face_recognition.compare_faces(self.encodeListKnown, encodeFace)
                    matches=face_recognition.compare_faces(self.encodeListKnown, encodeFace) #lower distance, better match
                    face_distance=face_recognition.face_distance(self.encodeListKnown, encodeFace)
                    matchIdx= np.argmin(face_distance)
                
                if(matches[matchIdx]):
                    y1, x2, y2, x1= faceLoc
                    y1, x2, y2, x1= y1*4, x2*4, y2*4, x1*4
                    bbox= 55+x1, 162+y1, x2-x1, y2-y1
                    imgBackground=cvzone.cornerRect(imgBackground,bbox, rt=0)
                    student=models.Student
                    student=student.fetchStudentInfo(student,self.student_IDs[matchIdx])
                    
                    # printing student info from supabase
                    print(student["first_name"] + " "+student["last_name"])
                    # print(self.face_confidence(face_distance[matchIdx]))  - still not working
            cv2.imshow("Face attendance", imgBackground) 
            cv2.waitKey(1)
            
        