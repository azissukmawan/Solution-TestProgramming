### Question
A company have 3 different capacity of milk bottle, which the milk bottle capacity is prime number between 0 to 30 litters (0 < Bottle x < 30). 

How many bottles from each different capacity does the company need to contain X litters of milk (100 < X < 10000000) such that the total number of bottles needed is the fewest? 

Example:
- Bottle 1 = 5 litter
- Bottle 2 = 7 litter
- Bottle 3 = 11 liter
  
X = 100

Answer:

Bottle 3 = 9 bottles, Bottle 1 = 1 bottle, Bottle 2 = 0 bottle, total = 10 bottles

or

Bottle 3 = 9 bottles, Bottle 1 = 0 bottle, Bottle 2 = 1 bottle, total = 10 bottles

### Output
```
  To fill 100 liters of milk, the minimum number of bottles required is 10, with the capabilities of bottle 1 = 1, bottle 2 = 1, and bottle 3 = 8.
  To fill 123 liters of milk, the minimum number of bottles required is 13, with the capabilities of bottle 1 = 0, bottle 2 = 5, and bottle 3 = 8.
```

### Conclusion
Kode tersebut merupakan solusi untuk masalah yang menanyakan bagaimana meminimalkan biaya pembelian botol dengan kapasitas berbeda untuk mengisi sejumlah susu. Kode tersebut mendefinisikan tiga kapasitas botol sebagai 5, 7, dan 11 liter, yang merupakan bilangan prima antara 0 dan 30. Kode ini juga mendefinisikan sebuah fungsi yang mengambil jumlah susu X sebagai input dan mengembalikan jumlah minimum botol yang dibutuhkan dan kapasitasnya. Fungsi ini menggunakan perulangan bertingkat untuk mencoba semua kombinasi botol yang mungkin dan memeriksa apakah botol-botol tersebut dapat mengisi X liter susu dengan tepat. Jika bisa, fungsi ini juga akan memeriksa apakah mereka menggunakan lebih sedikit botol daripada jumlah minimum saat ini. Jika ya, fungsi akan memperbarui jumlah minimum botol dan kapasitasnya. Fungsi tersebut kemudian mengembalikan jumlah minimum botol dan kapasitasnya.

### Setup
``` git clone https://github.com/azissukmawan/Solution-TestProgramming.git ```

``` cd Solution-TestProgramming ```

``` python Soal1/jawaban1.py ```
