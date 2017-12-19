#!/usr/bin/python3

import cv2
import numpy
from matplotlib import pyplot as plt

def main():
    citra = cv2.imread('citra/citra2.jpg')

    # membuat citra blur
    blur = cv2.blur(citra,(7,7))

    # menampilkan citra
    plt.subplot(121),plt.imshow(citra),plt.title("Gambar Asli")
    plt.xticks([]),plt.yticks([])

    plt.subplot(122),plt.imshow(blur),plt.title("Gambar Blur")
    plt.xticks([]),plt.yticks([])
    
    plt.show()

if __name__ == '__main__':
    main()
