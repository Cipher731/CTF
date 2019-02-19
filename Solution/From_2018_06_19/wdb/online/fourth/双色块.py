# 本题可以从gif中获取隐藏的png 从中可以得到key: ctfer2333
# 根据色块提取出二进制表示 得到密文: o8DlxK+H8wsiXe/ERFpAMaBPiIcj1sHyGOMmQDkK+uXsVZgre5DSXw==hhhhhhhhhhhhhhhh

import base64
from Crypto.Cipher import *
from PIL import Image

image: Image.Image = Image.open('out.gif')

data = ''
for y in range(24):
    for x in range(24):
        image.seek(y * 24 + x)
        frame = image.convert('RGB')
        pixel_coord = (10 * x, 10 * y)
        pixel = frame.getpixel(pixel_coord)
        if pixel == (0, 255, 0):
            data += '0'
        else:
            data += '1'

data_bytes = int(data, 2).to_bytes(len(data) // 8, 'big')
print(data_bytes)

cipher_base64 = b'o8DlxK+H8wsiXe/ERFpAMaBPiIcj1sHyGOMmQDkK+uXsVZgre5DSXw=='
cipher_text = base64.b64decode(cipher_base64)
print(cipher_text.hex())
key = b'ctfer233'

print(DES.new(key).decrypt(cipher_text))
