import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
from PIL import Image

mod = SourceModule("""
  __global__ void decode(float *img, float *msg, int message_length)
  {
 row = blockIdx.y * blockDim.y + threadIdx.y;
    col = blockIdx.x * blockDim.x + threadIdx.x;
    r, g, b, a = img.getpixel((col, row))
    # first pixel r value is length of message
    if row*col <= msg_length:
        msg += chr(r)
  }
  """)
encoded_image_file = "enc_mario.png"
img = Image.open(encoded_image_file)
r, g, b, a = img.getpixel((0, 0))
message_length = r

#do GPU stuff here
#allocate memory to gpu
image_gpu = cuda.mem_alloc(img.length)
message_gpu = cuda.mem_alloc(message_length)
#copy data to gpu
cuda.memcpy_htod(image_gpu, img)
#launch kernel
func = mod.get_function("decode")
func(image_gpu, message_gpu, message_length, block=(16,16,1))
#pull data from gpu
hidden_text = "abc"
cuda.memcpy_dtoh(hidden_text, message_gpu)
print("secret:", hidden_text)
