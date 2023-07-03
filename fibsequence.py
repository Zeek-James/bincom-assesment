#  Write a program to sum the first 50 fibonacci sequence
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# sum the first 50 Fibonacci numbers
sum = 0
for i in range(50):
    fib = fibonacci(i)
    sum += fib

print(sum)