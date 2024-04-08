# pyqt with opencv, still on experiment

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2, pickle, face_recognition
import numpy as np
import models

class Frames(QWidget):
    def __init__(self):
        super(Frames, self).__init__()

        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Camera()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Camera.stop()

class Camera(QThread):
    ImageUpdate = pyqtSignal(QImage)
    
    def __init__(self):
        
        pass
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        
        # load encodefile
        file= open("EncodeFile.p", 'rb')
        encodeListKnownWithIDs= pickle.load(file)
        file.close()
        studentIDs, encodeListKnown= encodeListKnownWithIDs
        
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                Image= cv2.resize(Image, (0,0), None, 0.25, 0.25) #make the video smaller, for small computational power

                FlippedImage = cv2.flip(Image, 1)
                
                faceCurrFrame= face_recognition.face_locations(Image) #looks for the face
                encodeCurrFrame= face_recognition.face_encodings(Image, faceCurrFrame) #matches the current face with the encodings, not the whole image
                
                
                for encodeFace, faceLoc in zip(encodeCurrFrame, faceCurrFrame):
                    matches=face_recognition.compare_faces(encodeListKnown, encodeFace)
                    matches=face_recognition.compare_faces(encodeListKnown, encodeFace) #lower distance, better match
                    faceDistance=face_recognition.face_distance(encodeListKnown, encodeFace)
                    # 
                    matchIdx= np.argmin(faceDistance)
                    
                    if(matches[matchIdx]):
                        # print("Face detected with ", studentIDs[matchIdx], " student ID")
                        # y1, x2, y2, x1= faceLoc
                        # y1, x2, y2, x1= y1*4, x2*4, y2*4, x1*4
                        # bbox= 55+x1, 162+y1, x2-x1, y2-y1
                        # imgBackground=cvzone.cornerRect(imgBackground,bbox, rt=0)
                        print(studentIDs[matchIdx])
                
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = Frames()
    Root.show()
    sys.exit(App.exec())