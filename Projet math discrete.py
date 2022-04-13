import numpy as np
A = np.array([[0.0, 5.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
              [3.0, 0.0, 2.0, 0.0, 1.0, 0.0, 4.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 4.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0],
              [1.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 2.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 3.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 4.0],
              [0.0, 0.0, 0.0, 3.0, 0.0, 5.0, 0.0, 0.0, 0.0, 2.0],
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0, 4.0, 0.0],
              ])
"collonne lien entrant, ligne lien sortant"
v = np.array([0.0219, 0.0325, 0.0373, 0.1099, 0.459, 0.0331, 0.0296, 0.1356, 0.0134, 0.1277])
alpha = 0.9

def pageRankLinear (A : np . matrix , alpha, v : np . array ):
    """
    – Input : Une matrice d’adjacence 1 A d’un graphe dirigé, pondéré et régulier G, un vecteur de personnalisation v, ainsi qu’un paramètre de téléportation α compris entre
    0 et 1 (0.9 par défaut et pour les résultats à présenter). Toutes ces valeurs sont nonnégatives.
    – Output : Un vecteur x contenant les scores d’importance des noeuds ordonnés dans
    le même ordre que la matrice d’adjacence.
    
    (I - alpha*P)^T * x = (1-alpha)*v
    Solve (I-alpha*P)^T * x = (1-alpha)*v with x^T*e = 1
    ->Solve (I-alpha*P)^T*x' = v and compute x = x'/||x'||'
    """

def pageRankPower (A, alpha, v):
    """
    – Input : Une matrice d’adjacence A d’un graphe dirigé, pondéré et régulier G, un vecteur de personnalisation v, ainsi qu’un paramètre de téléportation α compris entre 0
    et 1, α ∈]0,1[ (0.9 par défaut et pour les résultats à présenter).
    – Output : Un vecteur x contenant les scores d’importance des noeuds ordonnés dans
    le même ordre que la matrice d’adjacence.
    """
    n = len(A)
    x = v
    P = A
    iteration = 500000
    epsilon = 0.005
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += A[i][j]
        P[i] = A[i]/sum
    G = alpha * P + (1-alpha)/n * v
    print(P)
    print(G)
    for i in range(iteration):
        x = G @ x
        if i < 3:
            print(x)
        if np.linalg.norm(x-v, 1) < epsilon:
            print("finish")
            print(i)
            print(x)
            return x
        v = x
    
pageRankPower(A, alpha, v)