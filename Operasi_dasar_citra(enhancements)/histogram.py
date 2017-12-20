
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    citra = cv2.imread('../citra/citra3.bmp')

    # menampilkan gambar dan histogram
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(citra,cv2.COLOR_BGR2RGB))
    plt.xticks([]),plt.yticks([])



    warna = ('b','g','r')
    for i,col in enumerate(warna):
        histr = cv2.calcHist([citra],[i],None,[256],[0,256])
        plt.subplot(122)
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.title('Histogram (R,G,B)')

    plt.show()

if __name__ == '__main__':
    main()
