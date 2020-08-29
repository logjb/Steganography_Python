import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
from PIL import Image
mod = SourceModule("""
  __global__ void encode(float *img, float *message, float *encoded_img, int image_length, int message_length)
  {
        //hide text in the image
    row = blockIdx.y * blockDim.y + threadIdx.y;
    col = blockIdx.x * blockDim.x + threadIdx.x;
    printf("before")
    printf(img[col,row])
    r, g, b, a = img.getpixel((col, row));
    //length of hidden message goes first.
    if row == 0 and col == 0:
        message_bit = image_length;
    //still message left to hide
    elif row*col <= message_length:
        bit = msg[row*col - 1];
        message_bit = ord(bit);
    //else no message left to hide
    else:
        message_bit = r
    encoded_img.putpixel((col, row), (message_bit, g, b, a))
  }
  """)

original_image_file = "mario.png"
img = Image.open(original_image_file)
encoded_image_file = "enc_" + original_image_file
#no bigger than 255
secret_msg = "hello there"
image_length = img.size
message_length = len(secret_msg)

#do GPU stuff here
#allocate memory to gpu
image_gpu = cuda.mem_alloc(img.length)
encoded_image_gpu = cuda.mem_alloc(img.length)
message_gpu = cuda.mem_alloc(secret_msg.length)
#copy data to gpu
cuda.memcpy_htod(image_gpu, img)
cuda.memcpy_htod(encoded_image_gpu, img)
cuda.memcpy_htod(message_gpu, secret_msg)
#launch kernel
func = mod.get_function("encode")
func(image_gpu, message_gpu, encoded_image_gpu, image_length, message_length, block=(16,16,1))
#pull data from gpu
cuda.memcpy_dtoh(img, encoded_image_gpu)
img.save(encoded_image_file)
