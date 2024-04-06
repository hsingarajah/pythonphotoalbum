from PIL import Image
from PIL import ExifTags
from PIL.ExifTags import GPS
class MyPhoto:
    def __init__(self, Image = Image):
        self.myImage = Image
        self.myExif = self.myImage.getexif()
        self.myGPS = self.myImage.getexif().get_ifd(ExifTags.IFD.GPSInfo)

    def __init__(self):
        pass

    def initImage(self, Image= Image):
        self.myImage = Image
        self.myExif = self.myImage.getexif()
        self.myGPS = self.myImage.getexif().get_ifd(ExifTags.IFD.GPSInfo)

    def getImage(self):
        return self.myImage
    def  getExif(self):
        return self.myExif
    def getGPS(self):
        return self.myGPS



