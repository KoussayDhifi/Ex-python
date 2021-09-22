import random

#Sous Programmes

def saisir():
	n = int(input("n = "))
	while n<=2 or n>=10:
		n = int(input("n = "))
	return n


def remplir(n):
	M=[]
	for i in range(n):
		t=[]
		for j in range(n):
			t.append(chr(random.randint(65,90)))
		M.append(t)
	return M

def Affiche(M,n):
	ligne(M,n)
	colonne(M,n)
	diag(M,n)
	antiDiag(M,n)

def ligne(M,n):
	print("Ligne:")
	for i in range(n):
		for j in range(n):
			print(M[i][j],end="")
		print()

def colonne(M,n):
	print("Colonne:")
	for i in range(n):
		for j in range(n):
			print(M[j][i],end="")
		print()

def diag(M,n):
	print("Diag:")
	for i in range(n):
		for j in range(n):
			if (i==j):
				print(M[i][j],end="")
	print()
def antiDiag(M,n):
	print("AntiDiag:")
	for i in range(n):
		for j in range(n):
			if (i+j == n-1):
				print(M[i][j],end="")



#Programme Principale

n = saisir()
M = remplir(n)
Affiche(M,n)

#GG EZ




