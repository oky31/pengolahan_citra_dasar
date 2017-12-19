
import cv2
from matplotlib import pyplot as plt

def main():
    citra = cv2.imread('citra/citra3.bmp',0)

    # menambahkan kecerahan pada citra
    for i in range(len(citra)):
        for j in range(len(citra[0])):
            citra[i][j] = citra[i][j] + 40


    # plt.subplot(121),plt.imshow(citra),plt.title('Gambar RGB')
    # plt.show()
    cv2.imshow('tampil',citra)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
