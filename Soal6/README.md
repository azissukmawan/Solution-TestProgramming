### Question
Two players play a game with rules:
The game starts with a number of piles where piles: 2 < N < 1000
Each pile consists of matches with number: 0 < M < 1000
The player alternative takes the matches from 1 pile with the maximum they can take is 3, and minimum is 1.
Player cannot take match from different pile in their same turn.
The player who takes the last matches will win the game.
Write a program for this game which automatically played (bot, randomly) and announce the winner and the steps taken.


### Output
```
  The winner is Player 1!
The steps taken were:
Player 1 removed 3 match from pile 4
Player 2 removed 1 match from pile 1
Player 1 removed 1 match from pile 2
Player 2 removed 2 match from pile 2
Player 1 removed 1 match from pile 4
Player 2 removed 3 match from pile 4
Player 1 removed 1 match from pile 3
Player 2 removed 2 match from pile 3
Player 1 removed 1 match from pile 4
Player 2 removed 2 match from pile 3
Player 1 removed 2 match from pile 3
Player 2 removed 2 match from pile 1
Player 1 removed 3 match from pile 1
Player 2 removed 2 match from pile 1
Player 1 removed 1 match from pile 1
```

### Conclusion
Program ini pertama-tama menginisialisasi permainan dengan jumlah tumpukan acak dan jumlah korek api acak di setiap tumpukan. Kemudian mensimulasikan permainan dengan bot secara bergiliran mengeluarkan korek api dari tumpukan. Permainan berakhir ketika semua pertandingan telah dihapus, dan bot yang menghapus pertandingan terakhir dinyatakan sebagai pemenang. Program ini kemudian mencetak pemenang dan langkah-langkah yang diambil selama permainan. Harap diperhatikan bahwa program ini menggunakan pengindeksan berbasis nol untuk tumpukan, jadi tumpukan pertama adalah tumpukan 0. Selain itu, harap diperhatikan bahwa program ini mengasumsikan bahwa bot bermain secara acak.

### Setup
``` git clone https://github.com/azissukmawan/Solution-TestProgramming.git ```

``` cd Solution-TestProgramming ```

``` python Soal6/jawaban6.py ```
