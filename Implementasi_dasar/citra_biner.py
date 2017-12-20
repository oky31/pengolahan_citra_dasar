import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    # membaca citra grayscale
    citra = cv2.imread('../citra/citra4.bmp',0)

    # merubah menjadi citra biner
    # dengan fungsi bawaan openCv
    ret,tresh = cv2.threshold(citra,117,255,cv2.THRESH_BINARY)

    plt.subplot(121)
    plt.imshow(citra,'gray')
    plt.title("Citra Grayscale")
    plt.xticks([]),plt.yticks([])


    plt.subplot(122)
    plt.imshow(tresh,'gray')
    plt.title("Citra Biner")
    plt.xticks([]),plt.yticks([])

    plt.show()

if __name__ == '__main__':
    main()
