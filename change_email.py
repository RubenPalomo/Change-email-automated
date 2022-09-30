import os

def change(dir_name):
    if (dir_name != ""):
        files = os.listdir(dir_name)
    else:
        files = os.listdir()
    try:
        for file in files:
            f = open(file, 'r+')
            txt = f.read()
            f.write(txt.replace("example@adress.com", "my_email@gmail.com"))
            f.close()
        print("Files Modified Successfully")
    except:
        print("Files could not be modified")


change('')
