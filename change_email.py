import os

files = os.listdir('dir_name')
for file in files:
    f = open('dir_name/' + file, 'r')
    txt = f.read()
    f = open('dir_name/' + file, 'w')
    f.write(txt.replace("example@adress.com", "my_email@gmail.com"))
    f.close()
