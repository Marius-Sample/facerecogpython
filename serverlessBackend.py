import os
base_path="sampleClientSide/"
path="pic.jpg"


sr_code= "20-10100"
first_name="Haha"
last_name="Lele"
program="Mechanical Engineering"
degree="Bachelor"

os.rename(base_path+path, base_path+sr_code+".jpg")

