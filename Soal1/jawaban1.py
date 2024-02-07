# mendefinisikan tiga kapasitas botol sebagai bilangan prima antara 0 dan 30
bottle_1 = 5
bottle_2 = 7
bottle_3 = 11

def min_bottles(X):
    # menginisialisasi jumlah minimum botol dengan kapabilitas sebagai nol
    min_num = float("inf")
    cap_1 = 0
    cap_2 = 0
    cap_3 = 0
    # looping semua kombinasi botol yang mungkin
    for i in range(X // bottle_1 + 1):
        for j in range(X // bottle_2 + 1):
            for k in range(X // bottle_3 + 1):
                # cek apakah kombinasi dapat mengisi X liter susu
                if i * bottle_1 + j * bottle_2 + k * bottle_3 == X:
                    # cek apakah kombinasi menggunakan lebih sedikit botol daripada minimum saat ini
                    if i + j + k < min_num:
                        # update jumlah minimum botol dan kapabilitas
                        min_num = i + j + k
                        cap_1 = i
                        cap_2 = j
                        cap_3 = k
    # return minumum jumlah botol dan kapabilitas
    return min_num, cap_1, cap_2, cap_3

# test
X = 100
min_num, cap_1, cap_2, cap_3 = min_bottles(X)
print(f"To fill {X} liters of milk, the minimum number of bottles required is {min_num}, with the capabilities of bottle 1 = {cap_1}, bottle 2 = {cap_2}, and bottle 3 = {cap_3}.")

X = 123
min_num, cap_1, cap_2, cap_3 = min_bottles(X)
print(f"To fill {X} liters of milk, the minimum number of bottles required is {min_num}, with the capabilities of bottle 1 = {cap_1}, bottle 2 = {cap_2}, and bottle 3 = {cap_3}.")