
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    citra = cv2.imread('citra/citra3.bmp')

    # menampilkan gambar dan histogram
    warna = ('b','g','r')
    for i,col in enumerate(warna):
        histr = cv2.calcHist([citra],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()

if __name__ == '__main__':
    main()
