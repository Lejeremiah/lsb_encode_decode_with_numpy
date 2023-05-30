import numpy as np
from PIL import Image
import libnum

def lsb_encode(data):
    new_img = np.asarray(Image.new('RGB',(100,100),(255,255,255)),dtype=np.uint8)
    a,b,c = new_img.shape
    img_data = new_img.reshape(a*b*c)
    bin_data = libnum.s2b(data)

    bin_data_padding = bin_data+('0'*(len(img_data) - len(bin_data))) if len(img_data) > len(bin_data) else print('error')
    res_data = np.array([(i >> 1)*2+int(j) for i,j in zip(img_data,bin_data_padding)],dtype=np.uint8).reshape((a,b,c))
    img = Image.fromarray(res_data)
    img.save('./img.png')
def lsb_decode(img):
    img_data = np.array(Image.open(img).convert('RGB'))
    a,b,c = img_data.shape
    res_data = img_data.reshape(a*b*c)
    data = ''.join(str(i%2) for i in res_data)
    res = ''.join(chr(int(data[i:i+8],2)) for i in range(0,len(data),8))
    return res
lsb_encode('flag{test_flag}')
res = lsb_decode('./img.png')
print(res)
