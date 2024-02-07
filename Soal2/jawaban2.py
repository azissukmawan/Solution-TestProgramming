# definisi karbohidrat dan biaya per 100g untuk setiap item makanan
foods = {
    'Rice': {'carbs': 28, 'cost': None},
    'Corn': {'carbs': 21, 'cost': None},
    'Potato': {'carbs': 17, 'cost': None}
}

# definisi total karbohidrat yang dibutuhkan
total_carbs = 400

def min_cost(foods, total_carbs):
    # initialisasi biaya minimum dan jumlah yang sesuai
    min_cost = float('inf')
    amounts = {}

    # iterasi semua kombinasi jumlah yang mungkin
    for rice in range(0, total_carbs // foods['Rice']['carbs'] + 1):
        for corn in range(0, (total_carbs - rice * foods['Rice']['carbs']) // foods['Corn']['carbs'] + 1):
            potato = (total_carbs - rice * foods['Rice']['carbs'] - corn * foods['Corn']['carbs']) // foods['Potato']['carbs']
            if rice * foods['Rice']['carbs'] + corn * foods['Corn']['carbs'] + potato * foods['Potato']['carbs'] == total_carbs:
                cost = rice * foods['Rice']['cost'] + corn * foods['Corn']['cost'] + potato * foods['Potato']['cost']
                if cost < min_cost:
                    min_cost = cost
                    amounts = {'Rice': rice, 'Corn': corn, 'Potato': potato}

    return min_cost, amounts

# update biaya item makanan setiap hari
foods['Rice']['cost'] = 1.0
foods['Corn']['cost'] = 1.0
foods['Potato']['cost'] = 1.0

# kalkulasi dan cetak biaya minimum dan jumlah yang sesuai
cost, amounts = min_cost(foods, total_carbs)
print(f"Minimum cost: {cost}")
print(f"Amounts: {amounts}")
