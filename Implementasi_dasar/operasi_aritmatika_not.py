
import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():

    # membaca citra dan konversi ke grayscale
    citra_a = cv2.imread('../citra/citra1.jpg',0)

    ## menghitung histogram dengan fungsi bawaan openciv
    ## cv2.calcHist(images,channels,mask,histSize,ranges[,hist[,accumulate]])
    # hist = cv2.calcHist([citra],[0],None,[256],[0,256])

    ret,tresh = cv2.threshold(citra_a,117,255,cv2.THRESH_BINARY)

    citra_hasil_not = cv2.bitwise_not(tresh)


    plt.subplot(121)
    plt.imshow(tresh,'gray')
    plt.title('Citra Biner')
    plt.xticks([]),plt.yticks([])


    plt.subplot(122)
    plt.imshow(citra_hasil_not,'gray')
    plt.title('Hasil operasi\n (not)')
    plt.xticks([]),plt.yticks([])

    plt.show()


if __name__ == '__main__':
    main()
