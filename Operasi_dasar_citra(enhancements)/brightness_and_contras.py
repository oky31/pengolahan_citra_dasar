import cv2
import matplotlib.pyplot as plt


def main():
    # konstanta untuk kontras
    alfa = 1.1

    # konstanta untuk kecerahan
    beta = 5

    citra_awal = cv2.imread('../citra/citra3.bmp',0)
    citra = cv2.imread('../citra/citra3.bmp',0)

    # metode untuk meningkatkan kontras dan kecerahan
    # alfa * f(i,y) * beta
    for i in range(citra.shape[0]):
        for j in range(citra.shape[1]):
            citra[i][j] = alfa * citra[i][j] + beta

    plt.subplot(121)
    plt.imshow(citra_awal,cmap='gray')
    plt.title('Citra Asli')
    plt.xticks([]),plt.yticks([])

    plt.subplot(122)
    plt.imshow(citra,cmap='gray')
    plt.title('Perubahan\n kontras dan kecerahan')
    plt.xticks([]),plt.yticks([])

    plt.show()
if __name__ == '__main__':
    main()
