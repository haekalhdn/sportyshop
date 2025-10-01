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



## Tugas 4: Autentikasi, Session, dan Cookies di Django

### Langkah implementasi

#### 1) Registrasi: fungsi dan form

Pertama saya menyiapkan kebutuhan import, lalu membuat view untuk pendaftaran pengguna baru.

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```

View register memanfaatkan UserCreationForm. Saat menerima request POST dan datanya valid, user disimpan, muncul notifikasi sukses, lalu diarahkan ke halaman login.

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)
```

Saya juga membuat template register.html untuk merender form, menyertakan `{% csrf_token %}` agar aman dari serangan CSRF. Terakhir, fungsi register didaftarkan di urls.py supaya bisa diakses lewat urlpatterns.

#### 2) Login: autentikasi pengguna

Berikut impor yang kupakai. AuthenticationForm untuk validasi kredensial, sedangkan authenticate dan login dari Django mengurus proses autentikasi dan pembuatan sesi.

```python
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
```

Saya membuat view login_user sebagai gerbang login dan menyiapkan login.html sebagai antarmuka. Seperti sebelumnya, fungsi ini juga kuhubungkan di urls.py melalui urlpatterns.

#### 3) Logout: mengakhiri sesi

Supaya pengguna bisa keluar dari akunnya dan menutup sesi, saya menambahkan fungsi sederhana berikut.

```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

Tombol Logout kutaruh di main.html. Fungsinya diimpor ke urls.py dan rutenya ditambahkan ke urlpatterns.

#### 4) Batasi akses halaman main dan product_detail

Agar hanya pengguna yang sudah login yang bisa membuka halaman main dan product_detail, saya memakai dekorator bawaan Django login_required. Cukup tambahkan di view yang bersangkutan, misalnya show_main dan show_product.

```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    ...
```

Dengan begitu, pengunjung yang belum login akan diarahkan ke halaman login.

#### 5) Memakai cookies untuk menyimpan waktu login terakhir

Saya ingin menampilkan kapan terakhir kali pengguna login. Untuk itu, di views.py saya mengimpor datetime, HttpResponseRedirect, dan reverse, lalu memodifikasi bagian login agar menyimpan timestamp ke cookie.

```python
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```

Di fungsi show_main, saya mengambil nilai cookie tersebut agar bisa ditampilkan di halaman.

```python
context = {
    # konteks lain...
    'last_login': request.COOKIES.get('last_login', 'Never'),
}
```

Saat logout, cookie ini sekalian dihapus.

```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Terakhir, di main.html saya menambahkan `{{ last_login }}` untuk menampilkan waktu login terakhir.

#### 6) Mengaitkan model Product dengan User

Akhirnya, saya menghubungkan setiap produk dengan user. Tujuannya supaya user yang sedang login bisa memfilter dan melihat produk yang ia buat sendiri. Di model Product, saya menambahkan relasi ke User.

```python
from django.contrib.auth.models import User

user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
```

Di create_product pada views.py, setiap produk baru disimpan dengan atribut user mengarah ke request.user. Di halaman utama, saya menambahkan tombol filter supaya pengguna bisa memilih melihat semua produk atau hanya miliknya.

```html
<a href="?filter=all">
  <button type="button">All Products</button>
</a>
<a href="?filter=my">
  <button type="button">My Products</button>
</a>
```

Di product_detail.html, saya juga menampilkan nama pengguna yang mengunggah produk di bagian bawah untuk INFORMASI AUTHOR.

---

## PERTANYAAN

### 1) Apa itu Django `AuthenticationForm`? Apa kelebihan dan kekurangannya

`AuthenticationForm` adalah form bawaan untuk login yang memvalidasi kredensial sebagai bagian dari validasi form, dan dipakai oleh `LoginView` secara default. Kelebihannya, penggunaan dengan sistem auth dan session sehingga tidak perlu menulis form dari nol, serta bisa di‐subclass untuk kebutuhan kustom. Kekurangannya, kebutuhan non standar seperti login via email atau aturan akun khusus tetap memerlukan override atau backend kustom.

### 2) Apa bedanya autentikasi dan otorisasi di Django

Autentikasi memverifikasi identitas pengguna, sedangkan otorisasi menentukan apa yang boleh dilakukan pengguna yang sudah terautentikasi. Django menyediakan keduanya dalam satu sistem: autentikasi melalui `authenticate()`/`login()` dan otorisasi lewat permission, groups, serta pembatas akses seperti `login_required`.

### 3) Kelebihan dan kekurangan session vs cookies untuk menyimpan state

Cookie disimpan di browser, ringan dan tidak membebani server, tetapi kapasitas kecil dan rentan manipulasi jika tidak dikonfigurasi aman. Session di Django umumnya menyimpan data di server sementara browser hanya membawa session ID dalam cookie, sehingga lebih aman dan fleksibel tetapi menambah beban penyimpanan server.

### 4) Apakah cookies aman secara default? Bagaimana Django menanganinya

Cookie tidak otomatis aman. Risiko umum meliputi pencurian di koneksi tidak terenkripsi dan akses oleh skrip jika tidak diatur `HttpOnly`. Django menyediakan proteksi CSRF berbasis token, serta opsi penguatan lewat setting seperti `SESSION_COOKIE_HTTPONLY` dan `CSRF_COOKIE_SECURE` agar cookie tidak dibaca JavaScript dan hanya dikirim via HTTPS. Gunakan HTTPS, `HttpOnly`, `Secure`, dan nilai `SameSite` yang sesuai.

## Tugas 5

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Ketika ada beberapa CSS selector yang mengatur elemen yang sama, browser akan menentukan aturan mana yang digunakan berdasarkan prinsip specificity dan cascade. Prioritasnya dimulai dari inline style (paling tinggi), lalu ID selector, kemudian class, pseudo-class, dan attribute selector, setelah itu baru element/tag selector, sedangkan universal selector, inheritance, dan default browser style berada pada prioritas terendah. Jika specificity sama, aturan yang ditulis paling akhir akan dipakai, dan jika ada !important, maka aturan tersebut akan mengalahkan semuanya kecuali ada !important lain dengan tingkat specificity yang lebih tinggi.

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design adalah pendekatan dalam pengembangan web agar tampilan aplikasi menyesuaikan ukuran layar perangkat seperti desktop, tablet, atau smartphone, sehingga pengguna tetap nyaman tanpa harus melakukan zoom atau scroll horizontal. Konsep ini penting karena mayoritas pengguna internet saat ini mengakses melalui perangkat mobile, sehingga web yang tidak responsive akan menurunkan pengalaman pengguna dan ranking SEO. Misalnya, Instagram Web sudah menerapkan responsive design sehingga tampilannya menyesuaikan di layar ponsel maupun laptop, sedangkan beberapa situs lama atau portal berita kuno masih menggunakan ukuran tetap sehingga sulit dibaca di layar kecil.

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Dalam CSS box model, margin, border, dan padding memiliki fungsi berbeda. Margin adalah jarak luar elemen yang memisahkannya dari elemen lain di sekitarnya, border adalah garis yang mengelilingi elemen sebagai pembatas antara isi dan luar elemen, sedangkan padding adalah ruang di dalam border yang memisahkan konten dari garis batas elemen. Ketiganya dapat diatur dengan CSS, misalnya `margin: 20px;`, `border: 2px solid black;`, `padding: 15px;` untuk membuat jarak luar, garis tepi, dan jarak isi ke tepi.

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox dan grid layout adalah sistem layout modern di CSS yang memudahkan pengaturan elemen dibanding metode lama seperti float. Flexbox berfokus pada tata letak satu dimensi (horizontal atau vertikal) dan sangat cocok untuk mengatur item dalam baris atau kolom dengan properti seperti `display: flex;`, `justify-content;`, dan `align-items;`. Sementara itu, grid layout berfokus pada tata letak dua dimensi (baris dan kolom sekaligus), sehingga ideal untuk membuat struktur halaman kompleks menggunakan properti seperti `display: grid;`, `grid-template-columns;`, dan `gap;`. Maka, flexbox lebih cocok untuk mengatur isi komponen, sedangkan grid lebih tepat digunakan untuk mengatur keseluruhan layout halaman.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1.  **Membuat fungsi baru** `edit_product` untuk edit product dan `delete_product` untuk menghapus product di `views.py` dan hubungkannya ke http request di `urls.py`.
2.  **Mengatur konfigurasi static** di `settings.py` dan tambahkan folder baru bernama `static` di roots.
3.  **Membuat html baru** untuk `edit_product` dan `card_product` untuk digunakan nanti.
4.  **Membuat folder css** di `static/` dan tambahkan file `global.css` untuk css default/global.
5.  **Menambahkan konfigurasi tailwind** di `base.html` agar dapat menggunakan tailwind.
6.  **Menambahkan navbar.html** di `templates` roots untuk navigation bar website dan buatkan konfigurasi untuk mobile dan desktop agar dapat reponsive.
7.  **Menambahkan navbar** di `main.html` dengan `include`.
8.  **Mendesign seluruh templates** di main sesuai yang diinginkan dengan menggunakan tailwind dan html.
9.  Saya juga menggunakan `card_product.html` sebagai card untuk product-product yang ada dan hubungkan ke `main.html` dengan `include`.
10. Saya juga membuat folder baru di `static` bernama `image` untuk image yang digunakan pada aplikasi ini dan menambahkan image bernama `no-product` sebagai default image saat tidak ada product.
11. Lakukan "git add .", "git commit -m ", dan "git push origin " serta "git push PWS " setiap kali melakukan perubahan.

