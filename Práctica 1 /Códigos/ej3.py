import numpy as np

def suma():
    print(1 + 3)

    a = 7
    b = a + 1
    print("b =", b)

def vectores():
    # Vectores
    v = np.array([1, 2, 3, -1])
    w = np.array([2, 3, 0, 5])

    print("v + w =", v + w)
    print("2 * v =", 2 * v)
    print("v ** 2 =", v ** 2)

def matrices():

# Matrices (ejecutar los comandos uno a uno para ver los resultados)
    A = np.array([
        [1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4],
        [2, 3, 4, 5, 6],
        [0, 0, 1, 2, 3],
        [0, 0, 0, 0, 1]
    ])

    print(A)

    print(A[0:2, 3:5])
    print(A[:2, 3:])
    print(A[[0, 2, 4], :])

    ind = np.array([0, 2, 4])
    print(A[ind, ind])
    print(A[ind, ind[:, None]])

def complejos():
    # Números complejos
    print(1j * 1j)
    print((1 + 2j) * 1j)
 
def main() :
    suma()
    vectores()
    matrices()
    complejos()


if __name__ == "__main__":
    main()