import pyminizip

inputt = "SBL_MP.txt"

output = "save.zip"

password = "1234"

com_lvl = 5

pyminizip.compress(inputt, None, output, password, com_lvl)

from zipfile import ZipFile
import cv2

file_name = "save.zip"

with ZipFile(file_name, 'r') as zip:

    count = 0
    c = None
    while count < 3:
        try:
            string = input("Enter your password:  ")
            zip.extractall(pwd=bytes(string, 'utf-8'))
            c = "successful"
            if c == "successful":
                print(c)
                break

        except:
            a = print("You have entered a wrong password")
            print(a)
            if count == 2:
                camera = cv2.VideoCapture(0)
                return_value, image = camera.read()
                cv2.imwrite('FileLockImage' + '.png', image)
                del camera

        count += 1