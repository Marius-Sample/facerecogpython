import os
from supabase import create_client
import cv2, pickle, face_recognition
import supabase


class Utilities:
    def testFaceRefImport(file_name, sr_code, first_name, last_name, program, degree):
        url = "https://hphnqflbwqmfdvsfqkqi.supabase.co"
        key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhwaG5xZmxid3FtZmR2c2Zxa3FpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE1MjkwNjcsImV4cCI6MjAyNzEwNTA2N30.TA6JQ3L8ML7yv4f2Tst4dJ8MsokYmcc5JLKU2-iumiI"

        supabase = create_client(url, key)

        exists = supabase.table("Student").select("*").eq("sr_code",sr_code).execute()
        if(len(exists.data) > 0):
            print("Sr-code already exists")
            return False
        else:
            # storing data to database
            supabase.table("Student").insert({
                "sr_code": sr_code,
                "first_name": first_name,
                "last_name": last_name,
                "program": program,
                "degree": degree
            }).execute()
            new_filename=sr_code+".jpg"
            os.rename(file_name, new_filename)
            os.replace(new_filename, "students/" + new_filename) #move to students folder
            print("Done")
    
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
    
    def readFaceEncodings():
        # load face encodings from pickle file
        file= open("EncodeFile.p", 'rb')
        encodeListKnownWithIDs= pickle.load(file)
        file.close()
        return encodeListKnownWithIDs
    def matchSrToDB():
        data = supabase.table("Student").select("sr_code").execute()
        new_filenames=[]
        for i, row in enumerate(data.data):
            new_filenames.append(data.data[i]["sr_code"]+ ".jpg")

        # Directory containing the files
        directory = "students/"  # Replace with the path to your directory

        # Iterate over the files in the directory and rename them
        for index, filename in enumerate(os.listdir(directory)):
            # Construct the new filename
            new_filename = os.path.join(directory, new_filenames[index])
            # Construct the current filepath
            old_filepath = os.path.join(directory, filename)
            # Rename the file
            os.rename(old_filepath, new_filename)
