import PIL
from PIL import Image

import numpy

im = Image.open("mario.png")
px = numpy.array(im)
px = px.astype(numpy.float32)

str = "ABCD"
value = [elem.encode("hex") for elem in str]
values = [elem.encode("hex") for elem in str]
hidden_message = numpy.asarray(value)
print hidden_message
#for n in hidden_message:
    #print chr(map(ord, n.decode('hex'))[0])

print chr(64)

