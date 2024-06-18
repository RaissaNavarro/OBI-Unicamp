entrada = input("")
notas = input("")

N, K = map(int, entrada.split())
A = list(map(int, notas.split()))
A.sort(reverse= True)

print(A[K-1])














