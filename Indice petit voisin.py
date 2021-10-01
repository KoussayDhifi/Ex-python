#Sous Programme

def saisir():
    N = int(input(" N =  "))
    while not (3<=N<=10):
        N = int(input(" N =  "))
    return N

def remplir (N):
    T = []
    for i in range(N):
        x = int(input(f"T[{i}] = "))
        while not (x>=0):
            x = int(input(f"T[{i}] = "))
        T.append(x)
    return T

def voisin (T,N):
    c = 0
    T1 = []
    T2 = []
    for i in range(1,N-1):
        if (T[i]>T[i+1]) and (T[i]>T[i-1]):
            T1.append(T[i])
            c=c+1
            T2.append(i)
    return T1,T2,c

def indice (T1,T2,c):
    if c!=0:
        petit_indice = T2[0]
        parkour = 0
        for i in range(c):
            if (T1[i]<T1[parkour]):
                parkour = i
                petit_indice = T2[i]

        return petit_indice

    else:
        return -1



#Programme Principale


N = saisir()
T = remplir(N)
T1,T2,c = voisin(T,N)


print(f"L'indice de l'entier qui verifie la properite est {indice(T1,T2,c)}")





