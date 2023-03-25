##### **Load data CSV ke Excel:**

1. Buka aplikasi excel
2. Pilih Menu 'Data' selanjutnya lalu klik 'import text/csv' .
3. kemudian pilih file CSV yang akan di import lalu 'oke'.
4. Kemudian preview data akan ditampilkan kita bisa memilih opsi 'load' jika data tidak ada yang akan di filter jika masih akan melakukan filterisasi pada data silahkan memilih opsi 'Transform data' kemudian 'close & apply' perubahan.

Langkah-langkah load data ke Power Business Intelligence (PBI) :

##### **Load data CSV ke PBI:**

1. Buka PBI lalu klik 'Get data' di menu home.
2. Selanjutnya pilih format file 'Text/CSV'  pilih data yang akan di import ke PBI.
3. Kemudian preview data akan ditampilkan kita bisa memilih opsi 'load' jika data tidak ada yang akan di filter jika masih akan melakukan filterisasi pada data silahkan memilih opsi 'Transform data' kemudian 'close & apply' perubahan.
4. Selanjutnya ketik data sudah berhasil di import, Centang check box di bagian column data yang akan di visualisasi di menu 'Data' yang ada di bagian kanan.
5. Pilih bentuk virtualisasi di menu 'visualizations' yang ada di bagian kanan.

##### **Load data dari Mysql ke PBI:**

Untuk melakukan load dari dari database mysql ke PBI pastikan anda sudah menginstall Mysql Connector NET https://dev.mysql.com/downloads/file/?id=515908 agar bisa terkoneksi :

1. Pastikan anda sudah memiliki database dan data di Mysql.
2. Buka PBI lalu klik 'Get data' di menu home.
3. Pilih 'Database'.
4. Kemudian pilih 'MySQL Database' dan klik 'connect'.
5. Selanjutnya Masukkan localhost:3306 pada field input server dan 'nama_database' di field input databsase.
6. Setelah berhasil connect akan di tampilkan beberapa data yang ada di database anda, kemudian anda dapat memilih data mana yang akan di import ke PBI dengan cara centang check box data yang ada.
7. Kemudian preview data akan ditampilkan kita bisa memilih opsi 'load' jika data tidak ada yang akan di filter jika masih akan melakukan filterisasi pada data silahkan memilih opsi 'Transform data' kemudian 'close & apply' perubahan.
8. Selanjutnya ketik data sudah berhasil di import, Centang check box di bagian column data yang akan di visualisasi di menu 'Data' yang ada di bagian kanan.
9. Pilih bentuk virtualisasi di menu 'visualizations' yang ada di bagian kanan.

##### **Load data dari PostgreSQL local ke PBI:**

1. Pastikan anda sudah memiliki database dan data di PostgraSQL.
2. Buka PBI lalu klik 'Get data' di menu home.
3. Pilih 'Database'.
4. Kemudian pilih 'PostgreSQL Database' dan klik 'connect'.
5. Selanjutnya Masukkan localhost:5432 pada field input server dan 'nama_database' di field input database.
6. Kemudian isi username dengan postgres dan password sesuai password postgraSQL anda.
7. Setelah berhasil connect akan di tampilkan beberapa data yang ada di database anda, kemudian anda dapat memilih data mana yang akan di import ke PBI dengan cara centang check box data yang ada.
8. Kemudian preview data akan ditampilkan kita bisa memilih opsi 'load' jika data tidak ada yang akan di filter jika masih akan melakukan filterisasi pada data silahkan memilih opsi 'Transform data' kemudian 'close & apply' perubahan.
9. Selanjutnya ketik data sudah berhasil di import, Centang check box di bagian column data yang akan di visualisasi di menu 'Data' yang ada di bagian kanan.
10. Pilih bentuk virtualisasi di menu 'visualizations' yang ada di bagian kanan.

##### **Load data dari PostgraSQL Cloud Server ke PBI:**

1. Untuk melakukan load data dari PostgraSQL cloud server ke PBI pastikan anda sudah memiliki akun di elephant sql di https://www.elephantsql.com/ 
2. Kemudian klik menu New Instance dan lengkapi field input yang di sediakan.
3. Langkah selanjutnya, Connect PostgreSQL dengan Cloud server tadi di Pgadmin
4. Setelah membuka pgadmin, Anda bisa membuat server baru dengan cara klik kanan pada menu server ->  register -> server.
5. Isi nama server yang akan di buat di general, lalu bisa melengkapi koneksi di menu Connection.
6. Setelah berhasil terkoneksi maka akan muncul nama database anda, sesuaikan dengan nama database di elephant.
7. Untuk menambah data klik 'nama_database'  ->  'Schemas' -> Public -> Tables.
8. Klik kanan pada tabel lalu pilih 'Query tool'.
9. Tuliskan Query untuk membuat tabel dan insert data.
10. Setelah langkah tadi berhasil, Buka PBI 
11. Buka PBI lalu klik 'Get data' di menu home.
12. Pilih 'Database'.
13. Kemudian pilih 'PostgreSQL Database' dan klik 'connect'.
14. Selanjutnya Masukkan floppy.db.elephantsql.com pada field input server dan 'nama_database' di field input database.
15. Selanjutnya, isi Username, Password sesuai dengan instance yang ada di akun elephant.
16. Setelah berhasil connect akan di tampilkan beberapa data yang ada di database anda, kemudian anda dapat memilih data mana yang akan di import ke PBI dengan cara centang check box data yang ada.
17. Kemudian preview data akan ditampilkan kita bisa memilih opsi 'load' jika data tidak ada yang akan di filter jika masih akan melakukan filterisasi pada data silahkan memilih opsi 'Transform data' kemudian 'close & apply' perubahan.
18. Selanjutnya ketik data sudah berhasil di import, Centang check box di bagian column data yang akan di visualisasi di menu 'Data' yang ada di bagian kanan.
19. Pilih bentuk virtualisasi di menu 'visualizations' yang ada di bagian kanan.





