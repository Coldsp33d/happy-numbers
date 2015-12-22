def is_happy(n):
	t=[]
	while True:
		n=sum([int(x)**2 for x in str(n)])
		if n==1: return True
		elif n in t: return False

		t.append(n)

def find_happy(n):
	L=[]
	i=1
	while len(L) is not n:
		if is_happy(i): L.append(i)
		i+=1

	return L

if __name__=="__main__":
	
	print(find_happy(int(input())))
