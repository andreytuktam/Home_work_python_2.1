# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# Входные данные
# Входной файл INPUT.TXT содержит целое число N (1 < N ≤ 106).

# Выходные данные
# В выходной файл OUTPUT.TXT выведите ответ на задачу.

N = int(input("введите N: "))
k = 2
x = 1
if  1 < N <= 106:
    for i in range(N):
        while x > 0:
            difference = N // k
            if  N == k * difference:
                print("минимальный делитель", N, " = ", k)
                x = 0
            else:
                k = k + 1
else:
    print("перезапустите программу и введите 1 < N <= 106")