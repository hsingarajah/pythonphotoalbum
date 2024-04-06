import os
from PIL import Image
from PIL import ExifTags
from PIL.ExifTags import GPS
from my_photo import MyPhoto
import datetime
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myDir = os.getcwd()
    PhotoDir = 'MyPhotos'
    PDFDir = 'MyPDFs'
    PDFname = 'testoutput'

    PhotoArray = []

    files = (file for file in os.listdir(myDir + '/'+ PhotoDir)
             if os.path.isfile(os.path.join(myDir + '/'+ PhotoDir, file)))
    for file in files:  # You could shorten this to one line, but it runs on a bit.
        if file.endswith ('.JPG') or file.endswith('.jpg'):
            print(myDir + '/' + PhotoDir + '/' + file)
            tempObject = MyPhoto ()
            tempObject.initImage(Image.open(myDir + '/' + '/' + PhotoDir + '/' + file))
            PhotoArray.append( tempObject )

    #print (len(PhotoArray))


    for p in PhotoArray:
        print( p.getLatLong())

        myDate = p.getDateTime()
        print (myDate.strftime("%A %B %d, %Y \n%I:%M:S %p") )


# See PyCharm help at https://www.jetbrains.com/help/