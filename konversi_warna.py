#!/usr/bin/python3
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    # membaca citra dengan warna default
    citra = cv2.imread('citra/citra1.jpg')

    # mengkonversi warna citra dari RGB ke HSV
    citra_hsv = cv2.cvtColor(citra,cv2.COLOR_BGR2HSV)

    # menampilkan citra
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(citra,cv2.COLOR_BGR2RGB))
    plt.title('Gambar RGB')
    plt.xticks([]),plt.yticks([])

    plt.subplot(122)
    plt.imshow(citra_hsv)
    plt.title('Gambar HSV')
    plt.xticks([]),plt.yticks([])

    plt.show()

if __name__ == '__main__':
    main()
