import supabase

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
