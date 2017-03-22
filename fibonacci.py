# calculate the Fibonacci Series using recursion
# the function takes two arguments: n(number of iterations), k (reproduction rate)

def fibo(n, k):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibo(n - 1, k) + k * fibo(n - 2, k)
print fibo(29, 2)
