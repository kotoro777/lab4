import random
import time


def print_matrix(M, matr_name, tt):
    print("матрица " + matr_name + " промежуточное время = " + str(format(tt, '0.2f')) + " seconds.")
    for i in M:             # Делаем перебор всех строк матрицы
        for j in i:         # Перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()

try:

    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100: "))
    while row_q < 6 or row_q > 100:
        row_q = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    K = int(input("Введите число К= "))
    start = time.time()
    print("\n-----Результат работы программы-------")

    A, F, AF, FT = [], [], [], []  # Задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        AF.append([0] * row_q)
        FT.append([0] * row_q)
    time_next = time.time()
    print_matrix(F, "F", time_next - start)

    for i in range(row_q):       # Заполняем матрицу А
        for j in range(row_q):
            A[i][j] = random.randint(-10, 10)

    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)
    for i in range(row_q):      # F
        for j in range(row_q):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    C = []          # Задаем матрицу C
    size = row_q // 2
    for i in range(size):
        C.append([0] * size)

    for i in range(size):         # Формируем подматрицу С
        for j in range(size):
            C[i][j] = F[i][size + row_q % 2 + j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(C, "C", time_next - time_prev)

    cnt = 0
    multipl = 1
    for i in range(size):         # Обрабатываем подматрицу С
        for j in range(i + 1, size, 1):
            if j % 2 == 1 and j < size - 1 - i and C[i][j] > K:
                multipl *= C[i][j]
            elif j % 2 == 1 and j > size - 1 - i:
                cnt += 1
                
    if cnt > multipl:
        for i in range(1, size // 2, 1):   # Меняем подматрицу С
            for j in range(0, i, 1):
                C[i][j], C[i][size - j - 1] = C[i][size - j - 1], C[i][j]
        for i in range(size // 2, size, 1):
            for j in range(0, i, 1):
                C[i][j], C[i][size - j - 1] = C[i][size - j - 1], C[i][j]
        print_matrix(C,"C", time_next - time_prev)
        for i in range(size):             # Формируем матрицу F
            for j in range(size):
                F[i][size - row_q % 2 + j] = C[i][j]
    else:
        for j in range(row_q // 2 + row_q % 2, row_q, 1):
            for i in range(row_q // 2):
                F[i][j], F[row_q // 2 + row_q % 2 + i][j] = F[row_q // 2 + row_q % 2 + i][j], F[i][j]

    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)
    print_matrix(A, "A", 0)

    for i in range(row_q):   # K*A
        for j in range(row_q):
            A[i][j] = K * A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "K*A", time_next - time_prev)

    for i in range(row_q):      # K*A*F
        for j in range(row_q):
            s = 0
            for m in range(row_q):
                s = s + A[i][m] * F[m][j]
            AF[i][j] = s
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "K*A*F", time_next - time_prev)

    for i in range(row_q):       # FT
        for j in range(i, row_q, 1):
            FT[i][j], FT[j][i] = F[j][i], F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FT, "F^T", time_next - time_prev)

    for i in range(row_q):       # K*FT
        for j in range(row_q):
            FT[i][j] = K * FT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FT, "K*F^T", time_next - time_prev)

    for i in range(row_q):       # (K*A)*F+K*FT
        for j in range(row_q):
            AF[i][j] = AF[i][j] + FT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "(K*A)*F+K*F^T", time_next - time_prev)

    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")

except ValueError:
    print("\nЭто не число!")

except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
