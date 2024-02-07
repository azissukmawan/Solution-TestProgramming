import random

# define jumlah tumpukan dan jumlah pertandingan per tumpukan
N = random.randint(3, 10)  # Jumlah tumpukan
piles = [random.randint(1, 10) for _ in range(N)]  # Jumlah pertandingan per tumpukan

# define pemain
players = ['Player 1', 'Player 2']

steps = []
while sum(piles) > 0:
    # pemain saat ini adalah pemain yang sedang giliran
    player = players[0]

    # memilih tumpukan secara acak dan menghapus 1-3 pertandingan
    pile = random.choice([i for i in range(N) if piles[i] > 0])
    matches = random.randint(1, min(3, piles[pile]))
    piles[pile] -= matches

    # mencatat langkah
    steps.append((player, pile, matches))

    # pemain lain menjadi pemain saat ini
    players.reverse()

# Pemenang adalah pemain yang mengambil giliran terakhir
winner = players[1]

# tampikan pemenang dan langkah yang diambil
print(f"The winner is {winner}!")
print("The steps taken were:")
for step in steps:
    print(f"{step[0]} removed {step[2]} match from pile {step[1]+1}")

