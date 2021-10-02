def main():
	lista = random.sample(range(1, 100), 10)
	print("O.G. List: \n",lista,"\n")
	
	adjuntar(lista)
	sacar(lista)
	meter(lista)
	organizar(lista)
	reversa(lista)
	largo(lista)
	quitar(lista)
	indice(lista)
	
	return 0
	
def adjuntar(lista):
	n = random.sample(range(1, 100),1)
	lista.append(n)
	print("List after append: \n", lista,"\n")

def sacar(lista):
	lista.pop()
	print("List after pop: \n", lista,"\n")
	
def meter(lista):
	n = random.sample(range(1, 10),1)
	m = random.sample(range(1, 100),1)
	lista.insert(n, m)
	print("List after insert: \n", lista,"\n")
	
def quitar(lista):
	n = input(int("Number to remove: ")
	lista.remove(n)
	print("List after remove: \n", lista,"\n")
	
def organizar(lista):
	lista.sort()
	print("List after sort: \n", lista,"\n")

def reversa(lista):
	lista.reverse()
	print("List after reverse: \n", lista,"\n")
	
def largo(lista):
	print("Length of the list: ", len(lista))
	
def indice(lista):
	n = input(int("Number to check the index: ")
	print("The index of ", n, "is :", lista.index(n))
	
main()