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
