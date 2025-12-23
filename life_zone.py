#функция лямбда
radius = lambda Lstar, Lsun: (Lstar / Lsun) ** 0.5

def main():
    #светимость солнца
    Lsun = 3.86 * 10**33
    #ввод светимости звезды
    Lstar = float(input("dведите светимость звезды: "))
    #радиус
    d = radius(Lstar, Lsun) * 149597870700

    print("cредний радиус обитаемой зоны в метрах:", d)

if __name__ == "__main__":
    main()

