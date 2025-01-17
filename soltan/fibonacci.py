
"this is Fibonacci sequence of algorithm ."
def fibonacci(n):
	if n == 0:
		print('this value is not vlaid  for this function')
	if n < 0 :
		print('the number must be positive ')
	a, b = 0, 1	
	while b < n:
		for i in range(1, n):
			a, b  = b, a + b
	return b

print(fibonacci(10))

