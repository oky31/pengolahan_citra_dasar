
import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():

    # membaca citra dan konversi ke grayscale
    citra2 = cv2.imread('../citra/citra3.bmp',0)
    citra4 = cv2.imread('../citra/citra4.bmp',0)

    # rumbah citra menjadi citra binari
    ret,citra2_binary = cv2.threshold(citra2,117,255,cv2.THRESH_BINARY)
    ret,citra4_binary = cv2.threshold(citra4,117,255,cv2.THRESH_BINARY)

    # melakukan operasi or pada setiap pixel citra
    for i in range(citra2_binary.shape[0]):
        for j in range(citra2_binary.shape[1]):
            citra2_binary[i][j] = citra2_binary[i][j] | citra4_binary[i][j]

    plt.imshow(citra2_binary,'gray')
    plt.title('hasil')
    plt.xticks([])
    plt.yticks([])

    plt.show()


if __name__ == '__main__':
    main()
