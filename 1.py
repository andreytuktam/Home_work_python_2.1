# В первой строке входного файла INPUT.TXT записано 
# натуральное число N (1 ≤ N ≤ 100) – 
# число монеток. В каждой из последующих N строк содержится 
# одно целое число – 1 если монетка лежит решкой вверх и 0 если вверх гербом.

from random import randint

N = int(input("введите N: "))
p1 = 0
p2 = 0
if 1 <= N <= 100:
    for i in range(N):
        k = randint(0, 1)
        print(k)
        if k == 1:
            p1 = p1 + 1
        else:
            p2 = p2 + 1
    print({p1}, "монеток необходимо перевернуть, чтобы все были гербом ввкрх")
    print({p2}, "монеток необходимо перевернуть, чтобы все были решкой вверх")
else:
    print("перезапустите программу и введите 1 <= N <= 100")