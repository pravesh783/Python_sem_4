# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:08:48 2020

@author: pravesh

# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 
  
  
# String which represent the QR code 
s = "www.pravesh.epizy.com"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myqr.svg", scale = 8) 
"""
print("hello world")