import math

#функция для объема усеч. пирамиды
def pyramid_v(S1, S2, h):
    return (h / 3) * (S1 + S2 + math.sqrt(S1 * S2))

def main():
    #ввод:
    S1 = float(input("Введите площадь нижнего основания: "))
    S2 = float(input("Введите площадь верхнего основания: "))
    h = float(input("Введите высоту: "))

    #вычисляем объем:
    V = pyramid_v(S1, S2, h)

    print("Объем усеченной пирамиды(м куб.):", V)

if __name__ == "__main__":
    main()
