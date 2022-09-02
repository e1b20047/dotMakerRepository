import cv2
import numpy as np
from tkinter import filedialog
from PIL import Image

filenames=filedialog.askopenfilenames(
    title="画像ファイルを開く",
    filetypes=[("image file",".bmp .png .jpg .jpeg ")],
    initialdir="./"
    )
    #ダイアログを開く


for filename in filenames:
    buf=np.fromfile(filename,np.uint8)
    image = np.asarray(Image.open(filename).convert("RGBA"), dtype=np.uint8)
    #img = cv2.imread(filename)#ダイアログで取得したパスから画像読み出し
    img=cv2.imdecode(buf,cv2.IMREAD_UNCHANGED)
    img2=image.repeat(10, axis=0).repeat(10, axis=1)
    #print(img2.shape)
    Image.fromarray(img2).save("%s_10bai.png"%(filename))


