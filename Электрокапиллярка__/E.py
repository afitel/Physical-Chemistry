n = int(input())
if n == 1:
    print(2)
    exit(0)
#число последовательностей из 0(B) и 1(A) без 111
coun=[[[0 for i in range(2)] for j in range(2)] for k in range(n + 1)]
                                                # coun[len][prelast][last] - число последовательностей длины len,
                                                # заканчивающиеся на prelast,last без 111

coun[2][0][0] = coun[2][1][0] = coun[2][0][1] = coun[2][1][1] = 1

for len in range(3, n + 1, 1):
    coun[len][0][0] = coun[len - 1][0][0] + coun[len - 1][1][0]
    coun[len][0][1] = coun[len - 1][0][0] + coun[len - 1][1][0]
    coun[len][1][0] = coun[len - 1][0][1] + coun[len - 1][1][1]
    coun[len][1][1] = coun[len - 1][0][1]

print(coun[n][0][0] + coun[n][1][0] + coun[n][0][1] + coun[n][1][1])
'''zero = [0] * (n + 5) #количество последовательностей длины i с 0 на конце
one = [0] * (n + 5) #количество последовательностей длины i с 1 на конце
zero[1] = one[1] = int(1)
for i in range(2, n + 1, 1):
    zero[i] = zero[i - 1] + one[i - 1] #0 в конец можем добавить к любой последовательности длины i - 1
    one[i] = zero[i - 1] #1 можем добавить только к последовательности, заканчивающейся на 0
print(zero[n] + one[n])'''