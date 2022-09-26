import os

files = os.listdir('dir_name')
try:
    for file in files:
        f = open(file, 'r')
        txt = f.read()
        f = open(file, 'w')
        f.write(txt.replace("example@adress.com", "my_email@gmail.com"))
        f.close()
    print("Files Modified Successfully")
except:
    print("Files could not be modified")
