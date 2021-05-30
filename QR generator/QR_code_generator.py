import pyqrcode
import png
from pyqrcode import QRCode
  
  
# String which represents the QR code
s = "https://github.com/ojasg1"
  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "githubqr.svg"
url.svg("githubqr.svg", scale = 8)
  
# Create and save the png file naming "githubqr.png"
url.png('githubqr.png', scale = 6)
