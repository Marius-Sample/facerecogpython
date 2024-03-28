import os
from supabase import create_client
url = "https://hphnqflbwqmfdvsfqkqi.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhwaG5xZmxid3FtZmR2c2Zxa3FpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE1MjkwNjcsImV4cCI6MjAyNzEwNTA2N30.TA6JQ3L8ML7yv4f2Tst4dJ8MsokYmcc5JLKU2-iumiI"
supabase = create_client(url, key)

# data = supabase.table("Student").select("sr_code").execute()

# new_filenames=[]
# for i, row in enumerate(data.data):
#     new_filenames.append(data.data[i]["sr_code"]+ ".jpg")

# # Directory containing the files
# directory = "students/"  # Replace with the path to your directory

# # Iterate over the files in the directory and rename them
# for index, filename in enumerate(os.listdir(directory)):
#     # Construct the new filename
#     new_filename = os.path.join(directory, new_filenames[index])
#     # Construct the current filepath
#     old_filepath = os.path.join(directory, filename)
#     # Rename the file
#     os.rename(old_filepath, new_filename)





def fetchStudentInfo(sr_code):
    student_info = supabase.table("Student").select("*").eq("sr_code", sr_code).execute()
    return student_info.data
    