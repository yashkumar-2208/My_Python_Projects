import os 

def arrange_files(files, ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)
    pass

if __name__=="__main__":
    files = os.listdir()
    arrange_files(files,".jpg")