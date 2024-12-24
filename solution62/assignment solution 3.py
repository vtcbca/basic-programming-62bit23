def fibonacci_recursive(n, a=0, b=1, fib_sequence=None):
    if fib_sequence is None:
        fib_sequence = []
    if n == 0:
        return fib_sequence
    fib_sequence.append(a)
    return fibonacci_recursive(n - 1, b, a + b, fib_sequence)

n = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence with {n} terms: {fibonacci_recursive(n)}")