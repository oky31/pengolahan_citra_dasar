
import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():

    # membaca citra dan konversi ke grayscale
    citra_awal = cv2.imread('citra/citra1.jpg',0)
    citra = cv2.imread('citra/citra1.jpg',0)

    ## menghitung histogram dengan fungsi bawaan openciv
    ## cv2.calcHist(images,channels,mask,histSize,ranges[,hist[,accumulate]])
    hist = cv2.calcHist([citra],[0],None,[256],[0,256])


    ## merubah citra grayscale ke citra biner
    T = 110

    for i in range(citra.shape[0]):
        for j in range(citra.shape[1]):
            if citra[i][j] <= T:
                citra[i][j] = 1
            else:
                citra[i][j] = 0

    plt.subplot(121)
    plt.plot(hist)
    plt.title('Histogram')

    plt.subplot(122)
    plt.imshow(citra,'gray')
    plt.title('Citra Biner')
    plt.xticks([]),plt.yticks([])

    plt.show()


if __name__ == '__main__':
    main()
