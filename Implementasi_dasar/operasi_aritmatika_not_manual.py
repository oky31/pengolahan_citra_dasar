import copy
import cv2
import matplotlib.pyplot as plt

def main():
    # membaca citra dan konversi ke grayscale
    citra = cv2.imread('../citra/citra1.jpg',0)

    # rumbah citra menjadi citra binari
    ret,citra_binary = cv2.threshold(citra,117,255,cv2.THRESH_BINARY)

    citra_binary_not = copy.deepcopy(citra_binary)

    # melakukan operasi or pada setiap pixel citra
    for i in range(citra_binary.shape[0]):
        for j in range(citra_binary.shape[1]):
            citra_binary_not[i][j] = ~citra_binary[i][j]

    print(id(citra_binary))
    print(id(citra_binary_not))

    plt.subplot(121)
    plt.imshow(citra_binary,'gray')
    plt.title("Citra Biner")
    plt.xticks([]),plt.yticks([])

    plt.subplot(122)
    plt.imshow(citra_binary_not,'gray')
    plt.title("Hasil Operasi\n Not")
    plt.xticks([]),plt.yticks([])

    plt.show()

if __name__ == '__main__':
    main()
