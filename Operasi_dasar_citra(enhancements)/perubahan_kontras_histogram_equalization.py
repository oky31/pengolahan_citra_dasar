import cv2
import matplotlib.pyplot as plt

def main():
    # citra grayscale
    citra = cv2.imread("../citra/citra3.bmp",0)

    # meningkatkan kontras dengan metode histogram equalization
    equalization = cv2.equalizeHist(citra)

    # menampilkan citra
    plt.subplot(121)
    plt.imshow(citra,'gray')
    plt.title("Citra Asli")
    plt.xticks([]),plt.yticks([])

    plt.subplot(122)
    plt.imshow(equalization,'gray')
    plt.title("Hasil Perbaikan Kontras\n (Histogram equalization)")
    plt.xticks([]),plt.yticks([])

    plt.show()

if __name__ == "__main__":
    main()
