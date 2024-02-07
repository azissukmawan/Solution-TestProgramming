### Question
A mall wants to make a royalty program. From each 1,000,000 rupiahs spent on mall tenant, will award 10,000 rupiahs voucher to the registered                                                                                                                                    customer. To get the voucher, the customers need to show tenant invoice. This invoice will have unique transaction ID and can only be used once. This voucher has unique code which can only be used one. Each voucher has expired time for 3 months. Make a program and database to distribute and redeem the voucher (including registration and transaction).


### Output
```
['873856', '376555', '550346']
Voucher 873856 redeemed for 10000 rupiah!
Voucher 376555 redeemed for 10000 rupiah!
Voucher 550346 redeemed for 10000 rupiah!
```

### Conclusion
Program ini pertama-tama mendefinisikan database dan fungsi-fungsi untuk mendaftarkan pelanggan, mencatat transaksi, dan menukarkan voucher. Kemudian menguji program dengan mendaftarkan pelanggan, mencatat transaksi, dan menukarkan voucher. Hasilnya dicetak ke konsol. Harap diperhatikan bahwa program ini menggunakan database in-memory yang sederhana dan tidak menyimpan data di antara proses. Selain itu, perlu diketahui bahwa program ini mengasumsikan bahwa nama-nama pelanggan adalah unik. Terakhir, harap dicatat bahwa program ini menghasilkan kode voucher secara acak.

### Setup
``` git clone https://github.com/azissukmawan/Solution-TestProgramming.git ```

``` cd Solution-TestProgramming ```

``` python Soal7/jawaban7.py ```
