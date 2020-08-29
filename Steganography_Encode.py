from PIL import Image
import time
def encode_image(img, msg):
    if img.mode != 'RGBA':
        print "not RGBA"
        return
    # hide text in the image
    length = len(msg)
    encoded_image = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b, a = img.getpixel((col, row))
            # length of hidden message goes first.
            if row == 0 and col == 0:
                message_bit = length
                print(img.getpixel((col, row)))
            #still message left to hide
            elif index <= length:
                bit = msg[index - 1]
                message_bit = ord(bit)
            #else no message left to hide
            else:
                message_bit = r
            encoded_image.putpixel((col, row), (message_bit, g, b, a))
            index += 1
    return encoded_image
totalTime1 = time.time()
getDataTime1 = time.time()
original_image_file = "mario.png"
img = Image.open(original_image_file)
encoded_image_file = "enc_" + original_image_file
#no bigger than 255
#secret_msg = "hello there"
secret_msg = "BPCS-Steganography (Bit-Plane Complexity Segmentation Steganography) is a type of digital steganography. Digital steganography can hide confidential data (i.e. secret files) very securely by embedding them into some media data called vessel data."
getDataTime2 = time.time()
doWorkTime1 = time.time()
img_encoded = encode_image(img, secret_msg)
img_encoded.save(encoded_image_file)

doWorkTime2 = time.time()
totalTime2 = time.time()

totalTime = totalTime2 - totalTime1
doWorkTime = doWorkTime2 - doWorkTime1
getDataTime = getDataTime2 - getDataTime1

print("total time:",totalTime)
print("export and output time:",doWorkTime)
print("get data time:",getDataTime)



