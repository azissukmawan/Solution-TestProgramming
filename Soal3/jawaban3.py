def fibonacci_sum(X, Y, N):
    # inisiaisasi urutan Fibonacci dengan X dan Y
    sequence = [X, Y]

    # generate urutan lainnya
    for _ in range(2, N):
        sequence.append(sequence[-1] + sequence[-2])

    # kalkulasi jumlah bilangan genap dan ganjil
    sum_even = sum(n for n in sequence if n % 2 == 0)
    sum_odd = sum(n for n in sequence if n % 2 != 0)

    return sum_even, sum_odd

# test
X = 2
Y = 3
N = 3
sum_even, sum_odd = fibonacci_sum(X, Y, N)
print(f"Sum of even numbers: {sum_even}")
print(f"Sum of odd numbers: {sum_odd}")
