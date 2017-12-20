#!/usr/bin/python3
import cv2
import numpy as np


def main():
    # membaca gambar dengan bentuk grayscale
    citra = cv2.imread('../citra/citra3.bmp',cv2.IMREAD_GRAYSCALE)

    cv2.imshow('Gambar grayscale',citra)
    key = cv2.waitKey(0) & 0xFF

    if key == 27:
        cv2.destroyAllWindows()
    elif key == ord('s'):
        cv2.imwrite("citra_simpan_grayscale.png",citra)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
