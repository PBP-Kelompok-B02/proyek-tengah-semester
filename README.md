# Proyek Tengah Semester B02

## Aplikasi: **YumYogya**

### Anggota kelompok B02:
1. Abella Maya Santi - 2306275462
2. Fakhriyah Ghania Putri - 2306245466
3. Hizounya Maycinto Alkian - 2306245661
4. Lisa Margaretha Esron Tobing - 2306245541
5. Trias Fahri Naufal - 2306212096

## Deskripsi aplikasi
**YumYogya** adalah sebuah platform yang menampilkan daftar makanan yang tersedia di Yogyakarta lengkap dengan informasi tentang tempat makannya. Pengguna dapat mencari berbagai makanan dan menemukan rekomendasi tempat makan yang menyajikan makanan tersebut. Berikut ini adalah manfaat dari aplikasi:
- Aplikasi ini berguna bagi wisatawan atau penduduk lokal yang ingin mengeksplor kuliner di Yogyakarta.
- Pengguna bisa dengan cepat menemukan tempat makan sesuai makanan yang mereka cari serta mendapatkan informasi tambahan mengenai rating dan review makanan.
- Dengan adanya rating dan ulasan, pengguna dapat memilih tempat makan terbaik berdasarkan pengalaman orang lain.
- Pengguna tidak perlu repot-repot mencari informasi dari berbagai sumber karena semua sudah terintegrasi di satu tempat.

## Daftar modul
1. **Account & Dashboard**
Modul **Account dan Dashboard** berfungsi sebagai pusat autentikasi sekaligus pusat kendali akun bagi pengguna yang sudah login. Pengguna yang terautentikasi dapat melakukan **login**, **logout**, **penggantian password**, dan pengelolaan informasi terkait **profil** mereka. Hanya pengguna yang terautentikasi (bukan guest) yang dapat mengubah **password** dan **profil** mereka melalui dashboard. Jika **guest** mencoba mengakses dashboard, mereka akan langsung diarahkan ke *halaman login* atau **register**.

2. **Homepage**
Modul Homepage berfungsi sebagai beranda utama aplikasi yang menampilkan berbagai informasi mengenai makanan serta berbagai fitur yang dapat diakses oleh **user** maupun **guest**. Ketika makanan diklik, **user**/**guest** akan diarahkan ke **halaman detail makanan**.
Fitur-fitur yang akan diterapkan dalam modul ini:
     - **Pencarian dan Rekomendasi Makanan**
       Pengguna dapat mencari berbagai jenis makanan yang tersedia di Yogyakarta melalui **search bar**. Kemudian, makanan akan ditampilkan dengan urutan berdasarkan **rating tertinggi**.
     - **Filter dan Sorting**
       Pengguna bisa menggunakan **filter** untuk memilih makanan berdasarkan kategori tertentu, seperti **harga**, **jenis kuliner**, dan lainnya.
     
3. **Bookmark**
Modul **Bookmark** memberikan fitur kepada **user** untuk menyimpan makanan atau tempat makan favorit mereka agar dapat diakses kembali dengan mudah di lain waktu. Fitur ini hanya tersedia untuk **user** yang sudah login, sedangkan **guest** tidak memiliki akses untuk menambahkan bookmark dan akan diarahkan ke **halaman login** jika mencoba menggunakannya. Selain itu, pengguna juga dapat membuat label dan menyimpan makanan pada label tersebut 

4. **Forum**  
Modul **Forum** memberikan akses kepada **user** untuk membuat dan berpartisipasi dalam diskusi terkait topik tertentu. Pengguna dapat memulai diskusi, memberikan tanggapan, serta berbagi informasi atau pengalaman mereka. Fitur-fitur yang diterapkan dalam modul ini:
     - **Membuat Forum Diskusi** 
       Pengguna yang terautentikasi dapat membuat forum baru terkait topik tertentu, seperti makanan, tempat makan, atau rekomendasi kuliner di Yogyakarta.
     - **Memberi Tanggapan**  
       Pengguna yang terautentikasi juga dapat memberikan tanggapan atau komentar pada thread yang sudah ada, memperluas diskusi dan berbagi pendapat mereka.
     - **Akses Terbatas untuk Guest**  
       **Guest** hanya bisa melihat diskusi yang ada, tetapi tidak dapat membuat thread atau memberikan tanggapan. Mereka akan diarahkan ke halaman login jika mencoba berpartisipasi dalam diskusi.
       
5. **Detail Makanan**
Modul **Detail Makanan** berfungsi untuk menampilkan informasi lengkap tentang suatu makanan tertentu yang dipilih pengguna dari halaman **Homepage** atau **Bookmark**.
Informasi yang ditampilkan meliputi:
    - Nama makanan
    - Rating
    - Deskripsi makanan
    - Harga
    - Nama tempat makan
    - Alamat tempat makan

Pengguna juga dapat melihat **review** mengenai makanan tersebut. **Guest** dan **user** yang sudah login dapat mengakses dan melihat detail makanan pada halaman ini, tetapi **guest** tidak dapat menulis review atau menambah bookmark. **Review** memberikan akses bagi **pengguna** untuk memberikan ulasan atau penilaian terhadap makanan atau tempat makan yang telah mereka kunjungi. Pengguna dapat menilai berdasarkan bintang dan memberikan komentar disertai foto. Selain itu, pengguna juga dapat menghapus komentar milik mereka.


## Sumber initial dataset kategori utama produk
Dataset yang digunakan dalam aplikasi YumYogya berasal dari hasil scraping data melalui aplikasi layanan transportasi dan pemesanan makanan/minuman online, seperti Gojek, ShopeeFood, dan lainnya. Data yang diambil mencakup informasi terkait makanan dan tempat makan di Yogyakarta, seperti nama makanan, harga, rating, dan lokasi tempat makan. Dataset mencakup 100 jenis makanan atau minuman yang dijamin unik.


## Role atau peran pengguna beserta deskripsinya (karena bisa saja lebih dari satu jenis pengguna yang mengakses aplikasi)
- Guest : Dapat menjelajahi aplikasi, tetapi hanya bisa melihat informasi tanpa melakukan tindakan lebih lanjut, seperti memberikan ulasan atau menyimpan bookmark.
  
- User : Memiliki akses lebih luas, seperti menyimpan daftar makanan (bookmark) dan berinteraksi dengan konten, misalnya memberikan ulasan.

## Tautan deployment aplikasi
http://lisa-margaretha-yumyogya.pbp.cs.ui.ac.id
