import cv2
import matplotlib.pyplot as plt

def main():
    # membaca citra grayscale
    citra_awal = cv2.imread('../citra/citra2.jpg',0)
    citra = cv2.imread('../citra/citra2.jpg',0)

    # derajat keabuan citra
    L = 256

    # merubah citra grayscale ke citra negatif
    # citra_negatif = L - 1 - citra_awal
    for i in range(citra.shape[0]):
        for j in range(citra.shape[1]):
            citra[i][j] = L - 1 - citra[i][j]

    # menampilkan Citra
    plt.subplot(121)
    plt.imshow(citra_awal,'gray')
    plt.title('Citra Grayscale')
    plt.xticks([]),plt.yticks([])


    plt.subplot(122)
    plt.imshow(citra,'gray')
    plt.title('Citra Negatif')
    plt.xticks([]),plt.yticks([])

    plt.show()

if __name__ == '__main__':
    main()
