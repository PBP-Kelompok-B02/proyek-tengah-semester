# Proyek Tengah Semester B02

## Aplikasi: **YumYogya**

### Anggota kelompok B02:
1. Abella Maya Santi - 2306275462
2. Fakhriyah Ghania Putri - 2306245466
3. Hizounya Maycinto Alkian - 2306245661
4. Lisa Margaretha Esron Tobing - 2306245541
5. Trias Fahri Naufal - 2306212096

## Deskripsi aplikasi
**YumYogya** adalah sebuah platform yang menampilkan daftar makanan yang tersedia di Yogyakarta lengkap dengan informasi tentang tempat makannya. Pengguna dapat mencari berbagai makanan dan menemukan rekomendasi tempat makan yang menyajikan makanan tersebut. 
Berikut ini adalah manfaat dari aplikasi **YumYogya**:
- Aplikasi ini berguna bagi wisatawan atau penduduk lokal yang ingin mengeksplor kuliner di Yogyakarta.
- Pengguna bisa dengan cepat menemukan tempat makan sesuai makanan yang mereka cari serta mendapatkan informasi tambahan mengenai rating dan review makanan.
- Dengan adanya rating dan ulasan, pengguna dapat memilih tempat makan terbaik berdasarkan pengalaman orang lain.
- Pengguna tidak perlu repot-repot mencari informasi dari berbagai sumber karena semua sudah terintegrasi di satu tempat.

## Daftar modul
1. **Authentication & Dashboard**
Modul **Authentication dan Dashboard** berfungsi sebagai pusat autentikasi sekaligus pusat kendali akun bagi pengguna yang sudah login. Pengguna yang terautentikasi dapat melakukan **login**, **logout**, **penggantian password**, dan pengelolaan informasi terkait **profil** mereka. Hanya pengguna yang terautentikasi (bukan guest) yang dapat mengubah **password** dan **profil** mereka melalui dashboard. Jika **guest** mencoba mengakses dashboard, mereka akan langsung diarahkan ke *halaman login* atau **register**.

2. **Homepage**
Modul Homepage berfungsi sebagai beranda utama aplikasi yang menampilkan berbagai informasi mengenai makanan serta berbagai fitur yang dapat diakses oleh **user** maupun **guest**. Ketika makanan diklik, **user**/**guest** akan diarahkan ke **halaman detail makanan**.
  ### Fitur-fitur yang akan diterapkan dalam modul ini:
  1. **Pencarian dan Rekomendasi Makanan**
     Pengguna dapat mencari berbagai jenis makanan yang tersedia di Yogyakarta melalui **search bar**. Kemudian, makanan akan ditampilkan dengan urutan berdasarkan **ratin tertinggi**.
  2. **Filter dan Sorting**
     Pengguna bisa menggunakan **filter** untuk memilih makanan berdasarkan kategori tertentu, seperti **harga**, **jenis kuliner**, dan lainnya.
     
3. **Bookmark**
Modul **Bookmark** memberikan fitur kepada **user** untuk menyimpan makanan atau tempat makan favorit mereka agar dapat diakses kembali dengan mudah di lain waktu. Fitur ini hanya tersedia untuk **user** yang sudah login, sedangkan **guest** tidak memiliki akses untuk menambahkan bookmark dan akan diarahkan ke **halaman login** jika mencoba menggunakannya.

4. **Review**
Modul **Review** memberikan akses bagi **pengguna** untuk memberikan ulasan atau penilaian terhadap makanan atau tempat makan yang telah mereka kunjungi. Modul ini bertujuan untuk menambah informasi tentang kualitas makanan di suatu tempat makan sehingga dapat membantu pengguna dalam mengambil keputusan. Hanya **user** yang terautentikasi yang dapat menulis review untuk suatu makanan. Mereka bisa memberikan penilaian berupa *bintang** (misalnya dari 1 hingga 5) dan menambahkan **komentar** (opsional) untuk menjelaskan pengalaman mereka. Sementara itu, **guest** dan **user** dapat melihat semua review makanan yang tersedia, tetapi hanya **user** yang dapat memberikan review.
       
5. **Detail Makanan**
Modul **Detail Makanan** berfungsi untuk menampilkan informasi lengkap tentang suatu makanan tertentu yang dipilih pengguna dari halaman **Homepage** atau **Bookmark**.
Informasi yang ditampilkan meliputi:
    - Nama makanan
    - Rating
    - Deskripsi makanan
    - Harga
    - Nama tempat makan
    - Alamat tempat makan
Pengguna juga dapat melihat **review** mengenai makanan tersebut. **Guest** dan **user** yang sudah login dapat mengakses dan melihat detail makanan pada halaman ini, tetapi **guest** tidak dapat menulis review atau menambah bookmark.


## Sumber initial dataset kategori utama produk
csv


## Role atau peran pengguna beserta deskripsinya (karena bisa saja lebih dari satu jenis pengguna yang mengakses aplikasi) abel hizo
- Guest
  
- User
  
- Admin
  

## Tautan deployment aplikasi

