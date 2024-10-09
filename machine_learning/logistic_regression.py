#!/usr/bin/python

# Sıfırdan Lojistik Regresyon

# gerekli tüm kütüphaneleri içe aktarma

"""
Sınıflandırma problemi için lojistik regresyonun uygulanması
Yararlı kaynaklar:
Coursera ML kursu
https://medium.com/@martinpella/logistic-regression-from-scratch-in-python-124c5636b8ac
Katkı: K. Umut Araz
"""

import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets

# sınıflandırma problemlerinde hipotez fonksiyonu olarak kullanılan sigmoid fonksiyonu veya lojistik fonksiyon


def sigmoid_fonksiyonu(z: float | np.ndarray) -> float | np.ndarray:
    """
    Lojistik Fonksiyon olarak da bilinir.

                1
    f(x) =   -------
              1 + e⁻ˣ

    Sigmoid fonksiyonu, girişi 'x' pozitif arttıkça 1 değerine yaklaşır.
    Negatif değerler için tersi geçerlidir.

    Referans: https://en.wikipedia.org/wiki/Sigmoid_function

    @param z:  fonksiyona giriş
    @returns: 0 ile 1 arasında bir değer döner

    Örnekler:
    >>> float(sigmoid_fonksiyonu(4))
    0.9820137900379085
    >>> sigmoid_fonksiyonu(np.array([-3, 3]))
    array([0.04742587, 0.95257413])
    >>> sigmoid_fonksiyonu(np.array([-3, 3, 1]))
    array([0.04742587, 0.95257413, 0.73105858])
    >>> sigmoid_fonksiyonu(np.array([-0.01, -2, -1.9]))
    array([0.49750002, 0.11920292, 0.13010847])
    >>> sigmoid_fonksiyonu(np.array([-1.3, 5.3, 12]))
    array([0.21416502, 0.9950332 , 0.99999386])
    >>> sigmoid_fonksiyonu(np.array([0.01, 0.02, 4.1]))
    array([0.50249998, 0.50499983, 0.9836975 ])
    >>> sigmoid_fonksiyonu(np.array([0.8]))
    array([0.68997448])
    """
    return 1 / (1 + np.exp(-z))


def maliyet_fonksiyonu(h: np.ndarray, y: np.ndarray) -> float:
    """
    Maliyet fonksiyonu, tahmin edilen ve beklenen değerler arasındaki hatayı ölçer.
    Lojistik Regresyonda kullanılan maliyet fonksiyonuna Log Loss veya Cross Entropy Fonksiyonu denir.

    J(θ) = (1/m) * Σ [ -y * log(hθ(x)) - (1 - y) * log(1 - hθ(x)) ]

    Burada:
       - J(θ) eğitim sırasında minimize etmek istediğimiz maliyettir
       - m eğitim örneklerinin sayısıdır
       - Σ tüm eğitim örnekleri üzerindeki toplamı temsil eder
       - y belirli bir örnek için gerçek ikili etikettir (0 veya 1)
       - hθ(x) x'in pozitif sınıfa ait olma olasılığıdır

    @param h: sigmoid fonksiyonunun çıktısı. Bu, giriş örneği 'x'in pozitif sınıfa ait olma olasılığıdır

    @param y: giriş örneği 'x' ile ilişkili gerçek ikili etiket

    Örnekler:
    >>> tahminler = sigmoid_fonksiyonu(np.array([0.3, -4.3, 8.1]))
    >>> maliyet_fonksiyonu(h=tahminler,y=np.array([1, 0, 1]))
    0.18937868932131605
    >>> tahminler = sigmoid_fonksiyonu(np.array([4, 3, 1]))
    >>> maliyet_fonksiyonu(h=tahminler,y=np.array([1, 0, 0]))
    1.459999655669926
    >>> tahminler = sigmoid_fonksiyonu(np.array([4, -3, -1]))
    >>> maliyet_fonksiyonu(h=tahminler,y=np.array([1,0,0]))
    0.1266663223365915
    >>> tahminler = sigmoid_fonksiyonu(0)
    >>> maliyet_fonksiyonu(h=tahminler,y=np.array([1]))
    0.6931471805599453

    Referanslar:
       - https://en.wikipedia.org/wiki/Logistic_regression
    """
    return float((-y * np.log(h) - (1 - y) * np.log(1 - h)).mean())


def log_olabilirlik(x, y, ağırlıklar):
    skorlar = np.dot(x, ağırlıklar)
    return np.sum(y * skorlar - np.log(1 + np.exp(skorlar)))


# burada alpha öğrenme oranıdır, X özellik matrisidir, y hedef matristir
def lojistik_regresyon(alpha, x, y, max_iterasyon=70000):
    theta = np.zeros(x.shape[1])

    for iterasyon in range(max_iterasyon):
        z = np.dot(x, theta)
        h = sigmoid_fonksiyonu(z)
        gradyan = np.dot(x.T, h - y) / y.size
        theta = theta - alpha * gradyan  # ağırlıkları güncelleme
        z = np.dot(x, theta)
        h = sigmoid_fonksiyonu(z)
        j = maliyet_fonksiyonu(h, y)
        if iterasyon % 100 == 0:
            print(f"kayıp: {j} \t")  # her 100 iterasyonda bir kaybı yazdırma
    return theta


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    iris = datasets.load_iris()
    x = iris.data[:, :2]
    y = (iris.target != 0) * 1

    alpha = 0.1
    theta = lojistik_regresyon(alpha, x, y, max_iterasyon=70000)
    print("theta: ", theta)  # theta yani ağırlık vektörümüzü yazdırma

    def olasılık_tahmin(x):
        return sigmoid_fonksiyonu(
            np.dot(x, theta)
        )  # lojistik regresyon algoritmasından olasılık değerini tahmin etme

    plt.figure(figsize=(10, 6))
    plt.scatter(x[y == 0][:, 0], x[y == 0][:, 1], color="b", label="0")
    plt.scatter(x[y == 1][:, 0], x[y == 1][:, 1], color="r", label="1")
    (x1_min, x1_max) = (x[:, 0].min(), x[:, 0].max())
    (x2_min, x2_max) = (x[:, 1].min(), x[:, 1].max())
    (xx1, xx2) = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
    grid = np.c_[xx1.ravel(), xx2.ravel()]
    olasılıklar = olasılık_tahmin(grid).reshape(xx1.shape)
    plt.contour(xx1, xx2, olasılıklar, [0.5], linewidths=1, colors="black")

    plt.legend()
    plt.show()
