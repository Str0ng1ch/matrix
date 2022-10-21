from multiprocessing import Pool
import numpy as np
import os

N = 10
matrix1 = np.random.randint(0, 100, (N, N))
matrix2 = np.random.randint(0, 100, (N, N))
res = 0


def element(index, A=matrix1, B=matrix2):
    global res
    i, j = index
    res = 0
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res


def main():
    with Pool(os.cpu_count()) as pool:
        m = np.array(pool.map(element, [(i, j) for i in range(N) for j in range(N)])).reshape(N, N)
        print(m)


if __name__ == "__main__":
    main()
