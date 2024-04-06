import os
from PIL import Image
from PIL.ExifTags import GPS

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myDir = os.getcwd()
    PhotoDir = 'MyPhotos'
    PDFDir = 'MyPDFs'
    PDFname = 'testoutput'

    ImageArray = []
    ExifArray = []
    files = (file for file in os.listdir(myDir + '/'+ PhotoDir)
             if os.path.isfile(os.path.join(myDir + '/'+ PhotoDir, file)))
    for file in files:  # You could shorten this to one line, but it runs on a bit.
        if file.endswith ('.JPG') or file.endswith('.jpg'):
            print(myDir + '/' + PhotoDir + '/' + file)
            ImageArray.append(Image.open(myDir + '/' + '/' + PhotoDir + '/' + file))

    print (len(ImageArray))

    for i in ImageArray:
         ExifArray.append( i.getexif())

    for e in ExifArray:
        print("my pic")
        for k, v in e.items():
            print("Tag", hex(k), "Value", v)  # Tag 274 Value 2
    pdf_path = myDir + '/' + PDFDir + '/' + PDFname + '.pdf'


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
