import models, utils

def start():
    # Steps to import reference photo directly without client
    #   1. put reference photo in root folder, must be .jpg
    #   2. run utils.importFaceRefDirect(file_name, sr_code, first_name, last_name, program, degree)
    #   3. If success, it must print "Done"
    # EXAMPLE : 
    # sr_code= "21-21211"
    # utils.Utilities.testFaceRefImport("pic.jpg", sr_code, "Sample", "Name", "Computer", "Bachelor")
    # utils.Utilities.encodeFace("*") # you can encode more than two face references, must be a list, (*) only works as of now 

    
    # Example to print all encoded faces inside EncodeFile.p
    # sr_code, encoded=utils.Utilities.readFaceEncodings()
    # print(sr_code)
    models.FaceRecognition() # initialize face recognition
    

if __name__ == "__main__":
    start()