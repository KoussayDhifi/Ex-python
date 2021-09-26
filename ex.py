#Sous Programme

def saisir():
	n = int(input("n = "))
	while not(2<=n<=15):
		n = int(input("n = "))
	return n

def remplir(n):
	M = []

	for i in range(n):
		t = []
		for j in range(n):
			x = input(f"M[{i},{j}] = ")
			while not(65<=ord(x)<=90):
				x = input(f"M[{i},{j}] = ")

			t.append(x)
		M.append(t)
	return M


def Affiche(M,n):
	nl = 0
	nc = 0
	mc = ""
	ml = ""
	ch = ""
	for i in range(n):
		ch=""
		for j in range(n):
			ch+=M[i][j]
		if (ch==reverse(ch)):
			ml+=ch+"*"
			nl+=1

	for i in range(n):
		ch=""
		for j in range(n):
			ch+=M[j][i]
		if (ch == reverse(ch)):
			mc+=ch+"*"
			nc+=1
	ml = ml[0:len(ml)-1]
	mc = mc[0:len(mc)-1]
	print(ml)
	print(nl)
	print(mc)
	print(nc)

def reverse (x):
	s = ""
	for i in range(len(x)-1,-1,-1):
		s+=x[i]
	
	return s




#Programme Principale


n = saisir()
M = remplir(n)
Affiche(M,n)












