TUGAS 2
link pws : https://haekal-handrian-sportyshop.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).  
   1. Langkah pertama adalah membuat folder projek yaitu sportyshop, aktifkan virtual env, tulis requirements.txt. dan jalankan kemudian menginisialisasi Git, tulis .gitignore untuk menutup .env dan db.sqlite3.

   2. Buat proyek dan atur konfigurasi django-admin startproject sportyshop .Buat .env dan .env.prod, muat variabelnya di settings.py via python-dotenv agar dev dan production terpisah. Tambahkan ALLOWED\_HOSTS untuk dijalankan dengan lokal.

   3. Buat aplikasi dan model python manage.py startapp main, kemudian daftarkan di INSTALLED\_APPS. Definisikan Product pada bagian models.py dengan enam atribut wajib: name, price, description, thumbnail, category, is\_featured. Kemudian jalankan makemigrations dan migrate.

   4. Implementasi MVT, Buat view show\_main yang merender templates/main.html berisi nama aplikasi, nama, dan kelas(bagian ini saya edit agar web terlihat rapih). alurnya main/urls.py → path('', show\_main) lalu include('main.urls') di sportyshop/urls.py.

   5. Mengintegrasikan ke github dan juga runserver lokal serta ke pws. python manage.py runserver untuk cek halamanwebsite saya. Buat repo GitHub publik, set remote, dan git push origin master. Kemudian mendeploy ke PWS, Buat proyek PWS, isi Environs dengan isi .env.prod. Tambahkan domain PWS ke ALLOWED\_HOSTS. Jalankan perintah awal “Project Command” di PWS. Untuk keperluan update selanjutnya tinggal git push pws master dan git push origin master.

   

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.  
   <img width="1233" height="910" alt="Screenshot 2025-09-10 110647" src="https://github.com/user-attachments/assets/d49f96ad-00e0-444b-b0b8-338d844f0958" />

   Ketika pengguna membuka aplikasi Sportyshop lewat browser, mereka sebenarnya mengirimkan sebuah HTTP Request ke server Django. Permintaan ini pertama kali masuk ke berkas urls.py di proyek utama, yang berfungsi mencocokkan URL. Jika pola yang diminta cocok, maka request diarahkan ke urls.py milik aplikasi sportyshop. Dari sana, request dipetakan menuju fungsi di views.py, misalnya show\_main, yang berisi logika untuk menyiapkan data aplikasi. Jika halaman yang diminta perlu menampilkan daftar produk, fungsi ini akan berinteraksi dengan models.py untuk mengambil data dari database, contohnya Product.objects.all(). Data hasil query kemudian dibungkus dalam sebuah context dan diteruskan ke template HTML seperti main.html. Template ini akan menggabungkan data produk dengan tampilan visual aplikasi agar rapi dan mudah dibaca. Akhirnya, Django mengembalikan hasil tersebut dalam bentuk HTTP Response berupa halaman HTML, dan browser menampilkannya kepada pengguna sebagai antarmuka Sportyshop.  
     
3. Jelaskan peran settings.py dalam proyek Django\!  
   Peran [setting.py](http://setting.py) sangat penting mengingat dia asebagai pusat konfigurasi suatu proyek. Menyimpan INSTALLED\_APPS, DATABASES, ALLOWED\_HOSTS, SECRET\_KEY, pengaturan static file, serta pemisahan nilai untuk mode development dan production lewat variabel env. Tanpa settings.py, aplikasi tidak memiliki acuan yang konsisten.  
     
4. Bagaimana cara kerja migrasi database di Django?  
   Migrasi database di Django adalah proses menyamakan model di kode dengan struktur tabel di database. Saat kita mengubah model di Sportyshop, perintah makemigrations akan membuat berkas instruksi perubahan, lalu migrate menjalankan instruksi itu agar database benar-benar mengikuti skema model terbaru.  
     
5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?  
   Django dipilih untuk pemula karena arsitektur MVT-nya membuat alur aplikasi mudah dipahami, fitur bawaannya lengkap seperti ORM dan admin panel, serta dokumentasinya jelas. Framework ini juga memudahkan kita untuk membuat aplikasi cepat dan terstruktur.  
     
6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?  
   Feedback yang saya berikan positif terutama untuk kak Farel(REL), waktu kemarin ternyata saya memiliki masalah kemudian langsung diarahkan solusinya top\!

Referensi  
Tim Dosen PBP. (2024). PPT MTV Django Architecture. Fakultas Ilmu Komputer, Universitas Indonesia.

/////----------------/-----------------------------------///////////////

<br>Tugas 3 PBP<br>

1.  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
   Data delivery berperan sebagai "jembatan" komunikasi antara berbagai bagian aplikasi, misalnya frontend, backend, hingga layanan pihak ketiga. Tanpa adanya ini, setiap komponen akan berjalan sendiri-sendiri dan sulit saling bertukar informasi. Dengan data delivery, aplikasi bisa menampilkan data yang selalu up-to-date, interaksi pengguna lebih responsif, dan integrasi antar sistem menjadi lebih terstandar serta efisien.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
   XML dan JSON sama-sama bisa digunakan untuk pertukaran data, tapi JSON lebih unggul di aplikasi terbaru saat ini kenapa? karena JSON lebih singkat, strukturnya sederhana, mudah dibaca manusia, dan proses parsing yang lebih cepat. Disisi lain, XML memang mendukung struktur yang lebih kompleks, tapi terlalu verbose sehingga ukuran datanya jadi lebih besar. Popularitas JSON juga ikut naik karena langsung dengan JavaScript, sehingga kita sebagai user lebih mudah dengan aplikasi web lebih praktis dan akhirnya lebih banyak diadopsi oleh developer.

3.  Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
   is\_valid() dipakai untuk mengecek apakah data yang dikirim lewat form sudah sesuai dengan aturan validasi yang ditentukan. Django akan memverifikasi apakah field yang wajib diisi tidak kosong, tipe datanya benar, serta aturan tambahan lainnya terpenuhi. Kalau valid misalnya maka hasilnya bisa diakses lewat cleaned\_data untuk disimpan ke database. Kalau tidak valid, method ini akan mengembalikan False sekaligus menyimpan pesan error yang bisa ditampilkan di halaman form agar pengguna tau apa yang salah.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
   csrf\_token dibutuhkan sebagai lapisan keamanan untuk mencegah serangan Cross-Site Request Forgery (CSRF). Token ini memastikan bahwa request yang dikirim benar-benar berasal dari halaman aplikasi milik kita, bukan dari situs lain yang mencoba menyamar. Tanpa adanya token, seorang penyerang bisa mengeksploitasi sesi login pengguna untuk melakukan aksi berbahaya, misalnya mengirim form palsu yang secara otomatis mengubah data penting atau melakukan transaksi tanpa sepengetahuan pengguna. Dengan begitu, keberadaan csrf\_token sangat penting untuk menjaga keamanan aplikasi kita.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   1. Import HttpResponse dari django.http dan serializers dari django.core.  
   2. Membuat empat fungsi baru di views.py, yaitu show\_xml, show\_json, show\_xml\_by\_id, dan show\_json\_by\_id.  
   3. Pada show\_xml dan show\_json, kita mengambil semua objek Product, lalu mengubah hasil query menjadi format XML/JSON dan mengirimkannya sebagai response.  
   4. Pada show\_xml\_by\_id dan show\_json\_by\_id, mencari objek berdasarkan primary key, lalu mengembalikan data dalam format yang sesuai.  
   5. Menambahkan semua routing tersebut di main/urls.py agar bisa diakses lewat URL.  
   6. Membuat template main.html yang menampilkan daftar produk dengan tombol Add dan Detail(disini saya hanya mengubah news menjadi product menyesuaikan fungsi-fungsinya).  
   7. Menambahkan form di forms.py serta membuat template create\_product.html untuk menambahkan produk baru.  
   8. Membuat product\_detail.html,  untuk menampilkan informasi lengkap tiap produk.  
   9. Menambahkan models baru yaitu stock untuk stok barang, created\_at untuk waktu barang di upload, product\_views untuk melihat views.  
   10. Setiap ada perubahan kode, melakukan git add ., git commit, lalu git push ke repository GitHub maupun ke PWS.  
   11. Tidak lupa juga untuk setiap perubahan pada models selalu push migrations dan migrate
       
6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan? hmm kurang lenihnya aman kak..

Referensi
<br>Django Documentation, https://docs.djangoproject.com/en/5.0/<br>
<br>Json Website, https://www.json.org/json-en.html<br>
<br>Imaginary Cloud. (2023, September 14). JSON vs XML: the differences. Mariana Berga<br>
<br>,Rute Figueiredo. https://www.imaginarycloud.com/blog/json-vs-xml<br>

Foto Postman
<img width="2559" height="1520" alt="Screenshot 2025-09-16 225850" src="https://github.com/user-attachments/assets/6a72b1ff-918f-49cb-9689-4b046d442879" />


