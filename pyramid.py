import math

#функция для объема усеч. пирамиды
def pyramid_v(S1, S2, h):
    return (h / 3) * (S1 + S2 + math.sqrt(S1 * S2))

def main():
    #ввод:
    S1 = float(input("введите площадь нижнего основания: "))
    S2 = float(input("введите площадь верхнего основания: "))
    h = float(input("введите высоту: "))

    #вычисляем объем:
    V = pyramid_v(S1, S2, h)

    print("объем усеченной пирамиды(м куб.):", V)

if __name__ == "__main__":
    main()

