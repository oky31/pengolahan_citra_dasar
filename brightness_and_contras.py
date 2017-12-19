import cv2
import matplotlib.pyplot as plt


def main():
    alfa = 1
    beta = 40

    citra = cv2.imread('citra/citra3.bmp',0)

    for i in range(citra.shape[0]):
        for j in range(citra.shape[1]):
            citra[i][j] = alfa * citra[i][j] + beta

    plt.imshow(citra,cmap='gray')

    plt.show()
if __name__ == '__main__':
    main()
