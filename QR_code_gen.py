import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.linkedin.com/in/ishaan-choubey-b6b627245/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the svg file
url.svg("mylinkedin.svg", scale = 8) 