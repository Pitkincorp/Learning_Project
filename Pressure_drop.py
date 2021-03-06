r = int(input("Введите диаметр, мм: "))/2000  # в метрах
l = int(input("Введите длину, мм: ")) / 1000 # в метрах
V0 = l * 3.14 * r * r / 4
# dV значение протечки, м3
E = 2060 * 10 ** 6 # объемный модуль упругости жидкости (МПа)
# dP = dV * E / V0


def dP(dV):
    return dV/10**6 * E / V0

# Вывод значения падения давления при протечках от 0 до 20 мл
for i in range(21):
    print(f"dP = {int(dP(i))},Па при протечке {i} мл")
