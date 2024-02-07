def calculate_probability(X):
    # inisialisasi jumlah hasil sukses
    success_count = 0

    # total kemungkinan hasil saat menggulung tiga dadu 6 sisi
    total_outcomes = 6**3

    # iterasi semua kemungkinan hasil
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                if i + j + k == X:
                    success_count += 1

    # kalkulasi probabilitas
    probability = success_count / total_outcomes

    return probability

# test function dengan nilai X yang diberikan
X = 10
probability = calculate_probability(X)
print(f"The probability that the sum of the numbers rolled on three 6-sided dice is {X} is {probability}.")
