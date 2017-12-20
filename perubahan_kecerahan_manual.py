
import cv2
from matplotlib import pyplot as plt

def main():

    citra_sebelum = cv2.imread('citra/citra3.bmp',0)

    citra = cv2.imread('citra/citra3.bmp',0)

    # menambahkan kecerahan pada citra
    for i in range(len(citra)):
        for j in range(len(citra[0])):
            citra[i][j] = citra[i][j] + 40


    # menampilkan citra
    plt.subplot(121)
    plt.imshow(citra_sebelum,'gray')
    plt.title('Citra Asli')
    plt.xticks([]),plt.yticks([])

    plt.subplot(122)
    plt.imshow(citra,'gray')
    plt.title('Citra Dengan kecerahan')
    plt.xticks([]),plt.yticks([])


    plt.show()


if __name__ == '__main__':
    main()
