### Question
Given 5 boxes arranged from left to right. 

A	B	C	D	E
An object is put into the box randomly. For each step, the object is moving to another box which adjacent with current box randomly.
		Example: B > A or B > C, C > D or C > B
Make solution such that you can find the object within 7 steps. You can only use 1 pointer/selector to find the object.


### Output
```
  Step 1: Checking box C
  Object moved to box D
  Step 2: Checking box B
  Object moved to box E
  Step 3: Checking box D
  Object moved to box D
  Step 4: Checking box A
  Object moved to box E
  Step 5: Checking box E
  Object found in box E!
```

### Conclusion
Program ini pertama-tama menempatkan objek dalam kotak acak. Kemudian program ini memeriksa kotak-kotak dalam urutan C, B, D, A, E, mengulangi urutan ini seperlunya. Jika objek tidak ditemukan di dalam kotak, objek akan berpindah ke kotak yang berdekatan (jika ada). Pencarian akan berakhir ketika objek ditemukan atau setelah 7 langkah. Harap diperhatikan bahwa program ini mengasumsikan bahwa objek bergerak secara acak dan mungkin tidak selalu menemukan objek dalam 7 langkah karena keacakan pergerakan objek. Selain itu, perlu diketahui bahwa program ini menggunakan pengindeksan berbasis nol untuk langkah-langkahnya, sehingga langkah pertama adalah langkah 0.

### Setup
``` git clone https://github.com/azissukmawan/Solution-TestProgramming.git ```

``` cd Solution-TestProgramming ```

``` python Soal5/jawaban5.py ```
