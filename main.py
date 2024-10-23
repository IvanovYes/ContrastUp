from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
import math

def CalculateHistogramm(imageL):
    colums = imageL.shape[0]
    rows = imageL.shape[1]
    hist = np.zeros(255)
    for m in range(colums):
        for n in range(rows):
            hist[imageL[m, n]] = hist[imageL[m, n]] + 1
    return hist

def ContrustUp(imageL):
    hist = CalculateHistogramm(imageL)
    histEqulizer = np.zeros(255)
    colums = imageL.shape[0]
    rows = imageL.shape[1]
    histEqulizer[0] = hist[0]
    for k in range(1, 255, 1):
        histEqulizer[k] = histEqulizer[k - 1] + hist[k]
    for k in range(1, 255, 1):
        if histEqulizer[k] > 0:
            histEqulizerMin = histEqulizer[k]
            break
    L = np.zeros(255)
    for l in range(1, 255, 1):
        L[l] = round(((histEqulizer[l] - histEqulizerMin)/((colums * rows) - 1)) * 255)
    imageNew = imageL
    for m in range(colums - 1):
        for n in range(rows - 1):
            imageNew[m,n] = L[imageNew[m,n]]
    return imageNew

if __name__ == "__main__":
    print("Введите путь к изображению (используйте прямой слэш): ")
    frame = input()

    # Считываем изображение
    imageOrig = cv.imread(frame, 0)

    # Применение фильтрации для убирания шумов на изображении
    imageNew = cv.bilateralFilter(imageOrig, 3, 75, 75)

    imageNew = ContrustUp(imageNew)

    # Вывод обработанного изображения
    imageOrig = cv.cvtColor(imageOrig, cv.COLOR_BGR2RGB)
    imageNew = cv.cvtColor(imageNew, cv.COLOR_BGR2RGB)
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    ax[0].imshow(imageOrig)
    ax[0].set_title('Before')

    ax[1].imshow(imageNew)
    ax[1].set_title('After')

    plt.show()
    pass