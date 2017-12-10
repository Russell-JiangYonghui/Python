url = 'http://202.116.160.170/CheckCode.aspx '
from urllib.request import urlopen

path = urlopen(url)
import subprocess
from Pillow import Image
from Pillow import ImageOps


def cleanImage(imagePath):
    image = Image.open(imagePath)
    image.show()
    image = image.point(lambda x: 0 if x < 50 else 255)
    borderImage = ImageOps.expand(image, border=20, fill=255)
    borderImage.save("1.gif")


cleanImage(path)
p = subprocess.Popen(["tesseract", "1.gif", "captcha"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.wait()
f = open("captcha.txt", "rb")
b = f.read()
s = b.decode()
print(s.replace('\n', '').replace(' ', ''))