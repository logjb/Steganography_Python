import time
from PIL import Image
def decode(img):
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b, a = img.getpixel((col, row))
            # first pixel r value is length of message
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                msg += chr(r)
            index += 1
    return msg
totalTime1 = time.time()
getDataTime1 = time.time()
encoded_image_file = "enc_mario.png"
img = Image.open(encoded_image_file)
getDataTime2 = time.time()
doWorkTime1 = time.time()
hidden_text = decode(img)
print("secret:", hidden_text)
doWorkTime2 = time.time()
totalTime2 = time.time()

totalTime = totalTime2 - totalTime1
doWorkTime = doWorkTime2 - doWorkTime1
getDataTime = getDataTime2 - getDataTime1

print("total time:",totalTime)
print("export and output time:",doWorkTime)
print("get data time:",getDataTime)

