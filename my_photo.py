from PIL import Image
from PIL import ExifTags
from PIL.ExifTags import GPS
import datetime


class MyPhoto:
    def __init__(self, Image=Image):
        self.imageTimeStamp = None
        self.myImage = Image
        self.myExif = self.myImage.getexif()
        self.myGPS = self.myImage.getexif().get_ifd(ExifTags.IFD.GPSInfo)
        self.setLatLong()
        self.setDateTime()

    def __init__(self):
        self.imageTimeStamp = None
        self.myImage = None
        self.myExif = None
        self.myGPS = None
        self.myLatLong = None

    def setDateTime(self):
        tempExif = self.myExif
        datetimeString = tempExif[306].replace(' ', ':').split(':')

        for index, a in enumerate(datetimeString):
            datetimeString[index] = a.strip("0")
        datetimeInt = [eval(i) for i in datetimeString]
        self.imageTimeStamp = datetime.datetime(datetimeInt[0], datetimeInt[1], datetimeInt[2], datetimeInt[3],
                                           datetimeInt[4], datetimeInt[5])

    def getDateTime(self):
        return self.imageTimeStamp

    def setLatLong(self):

        tempGPS = self.myGPS
        myLat = 0.0
        myLong = 0.0
        #print(str(tempGPS[2]) + tempGPS[1])
        # print(str(tempGPS[4]) + tempGPS[3])

        myLat = tempGPS[2][0] + float(tempGPS[2][1]) / 60 + float(tempGPS[2][2]) / 3600
        if tempGPS[1] == 'S':
            myLat = myLat * -1

        myLong = tempGPS[4][0] + float(tempGPS[4][1]) / 60 + float(tempGPS[4][2]) / 3600
        if tempGPS[3] == 'W':
            myLong = myLong * -1

        self.myLatLong = (myLat, myLong)

    def getLatLong(self):
        return self.myLatLong

    def getLat(self):
        return self.myLatLong[0]

    def getLong(self):
        return self.myLatLong[1]

    def dms_to_dd(d, m, s):
        dd = d + float(m) / 60 + float(s) / 3600
        return dd

    def initImage(self, Image=Image):
        self.myImage = Image
        self.myExif = self.myImage.getexif()
        self.myGPS = self.myImage.getexif().get_ifd(ExifTags.IFD.GPSInfo)
        self.setLatLong()
        self.setDateTime()

    def getImage(self):
        return self.myImage

    def getExif(self):
        return self.myExif

    def getGPS(self):
        return self.myGPS
