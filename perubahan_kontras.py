
import cv2

def main():
    citra = cv2.imread("citra/citra3.bmp",0)

    hist = []
    dimensi = citra.shape

    for i in range(256):
        hist.append(0)

    for i in range(dimensi[0]):
        for j in range(dimensi[1]):
           hist[citra[i][j]] = hist[citra[i][j]] + 1

    jumlah_pixel = dimensi[0] * dimensi[1]

    for i in range(256):
        hist[i] = hist[i] / jumlah_pixel

    print(hist)

if __name__ == "__main__":
    main()
