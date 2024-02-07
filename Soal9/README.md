### Question
Given 2 matrix with size MxN and NxM. Make a program to multiply the matrix where 3<M<100 and 3<N<100.


### Output
```
[84, 90, 96]
[201, 216, 231]
[318, 342, 366]
```

### Conclusion
Program ini pertama-tama mendefinisikan fungsi yang mengalikan dua matriks. Hal ini dilakukan dengan mengulang-ulang baris matriks pertama dan kolom matriks kedua, dan untuk setiap pasangan baris dan kolom, program ini menghitung hasil perkalian titik dari baris dan kolom tersebut. Hasilnya adalah matriks baru yang merupakan hasil perkalian dari dua matriks input. Program ini kemudian menguji fungsi tersebut dengan dua matriks contoh dan mencetak hasilnya. Harap diperhatikan bahwa program ini mengasumsikan bahwa matriks input adalah valid (yaitu, mereka adalah daftar daftar angka, dan jumlah kolom di matriks pertama sama dengan jumlah baris di matriks kedua). Selain itu, harap diperhatikan bahwa program ini menggunakan pengindeksan berbasis nol untuk baris dan kolom, sehingga baris atau kolom pertama adalah baris atau kolom 0.

### Setup
``` git clone https://github.com/azissukmawan/Solution-TestProgramming.git ```

``` cd Solution-TestProgramming ```

``` python Soal9/jawaban9.py ```
