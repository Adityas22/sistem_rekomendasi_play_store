# SISTEM REKOMENDASI APLIKASI PLAY STORE DENGAN CONTENT BASED FILTERING DAN COLLABORATIVE FILTERING
### Dibuat : Aditya Septiawan

## Project Overview
Sistem rekomendasi aplikasi di Play Store sangat penting mengingat jumlah aplikasi yang terus meningkat dan beragamnya pilihan yang tersedia. Dengan lebih dari 3 juta aplikasi yang terdaftar di Google Play Store, pengguna sering kali merasa kewalahan dalam memilih aplikasi yang sesuai dengan kebutuhan mereka. Hal ini dapat menyebabkan pengalaman pengguna yang buruk dan mengurangi kepuasan pengguna terhadap platform tersebut. Oleh karena itu,Sistem rekomendasi dapat membantu pengguna menemukan aplikasi yang relevan berdasarkan minat dan kebutuhan mereka, sehingga mengurangi kebingungan saat memilih aplikasi[[1]](https://www.bhinneka.com/blog/ai-turut-berpartisipasi-pada-rekomendasi-di-play-store/).<br>

## Business Understanding
### Problem Statements
Berdasarkan latar belakang di atas, berikut ini merupakan rincian masalah yang dapat diselesaikan pada proyek ini:
1. Berdasarkan data yang tersedia, bagaimana membuat daftar rekomendasi aplikasi pada play store bagi pengguna sesuai dengan genre dengan metode pendekatan *content-based filtering*?
2. Berdasarkan data review dari pengguna, bagaimana membuat daftar rekomendasi aplikasi pada play store dengan metode pendekatan *collaborative filtering*?

### Goals
Tujuan dari proyek ini adalah:
1. Menghasilkan algoritma content-based filtering untuk merekomendasikan aplikasi kepada pengguna sesuai dengan preferensi genre mereka.
2. Menghasilkan algoritma collaborative filtering yang memanfaatkan data ulasan untuk memberikan rekomendasi aplikasi yang sesuai dengan preferensi pengguna lain.

### Solution Statements
Berdasarkan permasalahan sebelumnya, dapat diketahui bahwa akan dibuat dua buah model sistem rekomendasi aplikasi pada play store dengan metode pendekatan yang berbeda, yaitu *content-based filtering* dan *collaborative filtering*. Berikut adalah penjelasan dari kedua metode pendekatan tersebut.

#### 1. Content-Based Filtering
  Content-Based Filtering menggunakan atribut atau fitur dari item untuk merekomendasikan item yang mirip dengan yang telah disukai pengguna sebelumnya[[2]](https://www.ibm.com/topics/content-based-filtering?form=MG0AV3). Kelebihan CBF termasuk kemampuannya untuk memberikan rekomendasi yang dapat dijelaskan dan tidak bergantung pada interaksi pengguna lain. Namun, kelemahannya adalah potensi untuk menghasilkan rekomendasi yang monoton dan kesulitan dalam merekomendasikan item baru yang mungkin menarik bagi pengguna [[3]](https://thecleverprogrammer.com/2023/04/20/content-based-filtering-and-collaborative-filtering-difference/).

#### 2. Collaborative Filtering
  Collaborative Filtering (CF) menggunakan data interaksi pengguna lain yang memiliki preferensi serupa untuk merekomendasikan item[[2]](https://www.ibm.com/topics/collaborative-filtering?form=MG0AV3). Kelebihan CF adalah kemampuannya untuk merekomendasikan item yang mungkin tidak pernah dipertimbangkan oleh pengguna, karena ia memanfaatkan informasi dari komunitas pengguna secara keseluruhan. Namun, kelemahannya termasuk masalah cold-start bagi pengguna baru atau item baru, serta ketergantungan pada data interaksi yang cukup untuk menghasilkan rekomendasi yang akurat[[4]](https://developers.google.com/machine-learning/recommendation/collaborative/basics?hl=id).

## Data Understanding
Untuk membuat model yang dapat merekomendasikan plikasi pada play store kepada pengguna, tentunya membutuhkan dataset yang akan digunakan.<br>
Informasi Dataset:
Jenis | Keterangan
--- | ---
Title | Play Store Apps
Source | [Kaggle](https://www.kaggle.com/datasets/whenamancodes/play-store-apps)
published by | Aman Chauhan
License | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
Usability | 10.0

Pada Dataset ini terdapat 2 berkas csv diantaranya yaitu `googleplaystore.csv` yang memiliki jumlah data 9660 unique values  dan `googleplaystore_user_reviews.csv` yang memiliki jumlah data 1074 unique values

Pada berkas `googleplaystore.csv` memuat data-data aplikasi yang terdiri dari 10.841 baris dan memiliki 13  kolom, diantaranya adalah :
- App: 	Application name
- Category : 	Category the app belongs to
- Ratings : 	Overall user rating of the app (as when scraped)
- Reviews : 	Number of user reviews for the app (as when scraped)
- Size :	Size of the app (as when scraped)
- Installs : 	Number of user downloads/installs for the app (as when scraped)
- Type :	Paid or Free
- Price :	Price of the app (as when scraped)
- Content Rating : 	Age group the app is targeted at - Children / Mature 21+ / Adult
- Genre : 	An app can belong to multiple genres (apart from its main category). For eg, a musical family game will belong to
- Current Ver : 	Current version of the app available on Play Store (as when scraped)
- Android Ver : 	Min required Android version (as when scraped)

Pada berkas `googleplaystore_user_reviews.csv` memuat data-data Aplikasi yang terdiri dari 64.295   baris dan memiliki 5  kolom, diantaranya adalah :
- App : 	Name of app
- Translated Reviews : 	User review (Preprocessed and translated to English)
- Sentiment : Positive/Negative/Neutral (Preprocessed)
- Sentiment_polarity :	Sentiment polarity score
- Sentiment_subjectivity :	Sentiment subjectivity score

Adapun kondisi data seperti missing value :
1. `googleplaystore.csv`

| Kolom     | Missing Values |
|-----------|----------------|
| App       | 0              |
| Category  | 0              |
| Rating    | 1474           |
| Genres    | 0              |

2. `googleplaystore_user_reviews.csv`

| Kolom                 | Missing Values |
|-----------------------|----------------|
| App                   | 0              |
| Translated_Review     | 26,868         |
| Sentiment             | 26,863         |
| Sentiment_Polarity    | 26,863         |
| Sentiment_Subjectivity| 26,863         |

 
Berikut ini adalah hasil dari visualiasi `googleplaystore.csv`.
1. Rating
   ![Rating](https://github.com/Adityas22/sistem_rekomendasi_play_store/raw/main/image/Rating.png)
   Visualisasi data rating ini cenderung mendapatkan penilaian yang tinggi dari pengguna, dengan puncak frekuensi pada rating 5.0. Namun, grafik juga menunjukkan adanya sebaran rating yang cukup luas, dengan frekuensi yang signifikan pada rating 4.5, 4.0, dan 3.5, mengindikasikan bahwa pengguna memberikan penilaian yang beragam.
2. Genre
   ![Genre](https://github.com/Adityas22/sistem_rekomendasi_play_store/raw/main/image/Genres.png)
   Visualisasi data genre ini terlihat bahwa aplikasi di platform ini didominasi oleh kategori "Tools" atau utilitas, yang menunjukkan jumlah jauh lebih besar dibandingkan genre lainnya. Namun, terdapat pula beberapa genre dengan distribusi yang cukup merata, seperti "Entertainment", "Education", dan "Medical", menandakan keberagaman preferensi pengguna. Di sisi lain, ada beberapa genre niche atau khusus, seperti "Travel & Local", "Sports", dan "Dating", yang mengindikasikan adanya segmentasi pasar yang perlu dipertimbangkan. Selain itu, terdapat peluang pengembangan di genre-genre yang saat ini kurang terwakili, seperti "News & Magazines" dan "Books & Reference".

Berikut ini adalah hasil dari visualiasi `googleplaystore_user_reviews.csv`.
1. Sentiment_polarity <br>
   ![Sentiment_polarity](https://github.com/Adityas22/sistem_rekomendasi_play_store/raw/main/image/sentiment_polarity.png) <br>
   Visualisasi data Sentiment_polarity menunjukkan bahwa mayoritas ulasan atau sentimen yang diberikan pengguna cenderung berada pada posisi netral, dengan puncak frekuensi yang dominan pada polaritas 0.00.
3. Sentiment_subjectivity <br>
   ![Sentiment_subjectivity](https://github.com/Adityas22/sistem_rekomendasi_play_store/raw/main/image/Sentiment_Subjectivity.png) <br>
   Visualisasi data Sentiment_subjectivity ini Terlihat puncak yang dominan pada nilai subjektivitas 0.8, mengindikasikan bahwa sebagian besar ulasan atau sentimen yang diberikan pengguna cenderung bersifat sangat subjektif.


## Data Preparation
Proses persiapan data pada masing-masing metode dilakukan secara terpisah karena bentuk data yang dibutuhkan pada setiap model dari kedua metode tersebut berbeda.
### 1. Content-Based Filtering
- Untuk menyederhanakan analisis, kita akan menghapus beberapa kolom dari dataset `googleplaystore.csv` yang tidak diperlukan untuk model content-based filtering. Kolom yang akan dihapus adalah:'Reviews', 'Size', 'Price', 'Type', 'Installs', 'Content_Rating', 'Last_Updated', 'Current_Ver', 'Android_Ver'. Sekarang kita fokus pada kolom-kolom :'App', 'Category', 'Rating', 'Genres'.
- Menggabungkan`googleplaystore.csv` dengan dataset `googleplaystore_user_reviews.csv`. Penggabungan ini akan memberikan pandangan yang lebih komprehensif tentang aplikasi, dataset yang digabungkan akan disimpan dalam variabel baru bernama all_apk_user yang berisikan 125401 rows × 8 columns.
- Karena setiap aplikasi seharusnya hanya muncul sekali dalam dataset kita, kita perlu memeriksa dan menghapus entri duplikat berdasarkan kolom App dan yang memiliki nilai kosong. Ini memastikan bahwa dataset kita tetap bersih dan akurat. Sekarang disimpan pada variable `preparation`.
- Setelah memastikan bahwa dataset kita bersih dari nilai hilang dan duplikat, kita dapat mengonversi kolom tertentu menjadi list. Misalnya, kita bisa mengonversi kolom Genres dan Rating menjadi list untuk memudahkan pemrosesan selanjutnya.
- Setelah mengonversi data menjadi list, kita dapat membuat dictionary untuk menyimpan pasangan key-value. Dictionary ini bisa digunakan untuk menyimpan informasi penting, seperti mengaitkan setiap aplikasi dengan genre dan Rating-nya.
- Menggunakan TfidfVectorizer dari pustaka sklearn untuk menghitung nilai TF-IDF untuk kolom Genres, mengubah data teks menjadi representasi numerik. Kemudian proses mapping ini memungkinkan kita untuk dengan mudah mengakses dan mengelola informasi terkait setiap aplikasi.
````
  array(['action', 'adventure', 'arcade', 'art', 'auto', 'beauty', 'board',
       'books', 'brain', 'business', 'casual', 'comics', 'communication',
       'creativity', 'dating', 'demo', 'design', 'drink', 'editors',
       'education', 'educational', 'entertainment', 'events', 'finance',
       'fitness', 'food', 'games', 'health', 'home', 'house', 'libraries',
       'lifestyle', 'local', 'magazines', 'maps', 'medical', 'music',
       'navigation', 'news', 'parenting', 'personalization',
       'photography', 'play', 'players', 'playing', 'pretend',
       'productivity', 'puzzle', 'racing', 'reference', 'role',
       'shopping', 'simulation', 'social', 'sports', 'strategy', 'tools',
       'travel', 'vehicles', 'video', 'weather'], dtype=object)
````


### 2. Collaborative Filtering
- Dataset yang dipakai adalah `googleplaystore_user_reviews.csv`, kemudian membersihkan dataset dari nilai hilang.
- Langkah selanjutnya adalah membagi dataset `user_clean` menjadi dua subset: 80% untuk pelatihan (training) dan 20% untuk pengujian (testing). Pembagian ini penting untuk memastikan bahwa model yang kita latih tidak terpapar pada data yang sama ketika kita mengujinya.

## Modeling and Result
Berdasarkan pernyataaan solusi sebelumnya, proses pemodelan dibagi menjadi dua metode pendekatan, yaitu metode content-based filtering dan metode collaborative filtering. Berikut adalah penjelasan dan tahapan dalam proses pemodelan dari masing-masing metode pendekatan.
### 1. Content-Based Filtering
Proses dimulai dengan TfidfVectorizer dari sklearn yang digunakan untuk mengekstrak fitur dari kolom Genres dengan menghitung Term Frequency-Inverse Document Frequency (TF-IDF), yang mengubah teks menjadi representasi numerik. Proses ini melibatkan fitting model pada data genre untuk menghitung nilai IDF dan kemudian mentransformasikannya menjadi matriks TF-IDF `(Dalam hal ini ukuran matriks 816 X 61)`. Matriks ini menunjukkan bobot setiap kata dalam genre untuk setiap aplikasi dan disimpan dalam sebuah DataFrame untuk analisis lebih lanjut. <br>
Setelah itu, cosine similarity dihitung untuk mengukur seberapa mirip dua aplikasi berdasarkan vektor TF-IDF mereka, dengan nilai berkisar antara 0 (tidak mirip) hingga 1 (sangat mirip). Matriks cosine similarity disusun dalam DataFrame, memudahkan visualisasi aplikasi yang mirip satu sama lain. Fungsi `apk_recommendations_based` kemudian diimplementasikan untuk memberikan rekomendasi berdasarkan nama aplikasi yang dimasukkan pengguna, mencari aplikasi mirip melalui nilai cosine similarity, dan menghapus aplikasi yang sama dari daftar rekomendasi. Rekomendasi ini diurutkan berdasarkan rating, dan sejumlah aplikasi ditampilkan sesuai parameter top n yang ditentukan `(n=10)`.<br>
Hasil dari proses ini pengguna memasukkan nama aplikasi dan menerima rekomendasi aplikasi lainnya yang memiliki kesamaan genre dan rating yang tinggi, dapat dilihat seperti dibawah ini: 

Rekomendasi untuk APK 'GoBank':
| App                            | Genres   |   Rating |   Sentiment_Polarity |   Sentiment_Subjectivity | Sentiment   |
|--------------------------------|----------|----------|----------------------|--------------------------|-------------|
| Associated Credit Union Mobile | Finance  |      4.7 |           -0.0555556 |                 0.244444 | Negative    |
| BZWBK24 mobile                 | Finance  |      4.5 |           -0.0443452 |                 0.480357 | Negative    |
| Bank of America Mobile Banking | Finance  |      4.4 |           -0.0717172 |                 0.253535 | Negative    |
| Acorns - Invest Spare Change   | Finance  |      4.3 |            0.283333  |                 0.469444 | Positive    |
| Amex Mobile                    | Finance  |      4.3 |            0.275     |                 0.55     | Positive    |
| BBVA Compass Banking           | Finance  |      4.3 |            1         |                 0.3      | Positive    |
| BankMobile Vibe App            | Finance  |      4.3 |            0.110606  |                 0.684242 | Positive    |
| BBVA Spain                     | Finance  |      4.2 |            0.333333  |                 0.6      | Positive    |
| ACE Elite                      | Finance  |      4.1 |            0         |                 0        | Neutral     |
| Banorte Movil                  | Finance  |      4.1 |            0.328571  |                 0.535119 | Positive    |

### 2. Collaborative Filtering
Dataset yang sudah dibagi menjadi dua bagian: train set dan test set pada data preparation kemudian langkah selanjutnya adalah menerapkan algoritma KNN untuk menemukan aplikasi yang mirip.<br>
Model KNN dilatih dengan metrik cosine similarity dan algoritma brute, yang mengukur jarak antar aplikasi berdasarkan sudut vektor. Fungsi `find_similar_items_knn` memungkinkan pengguna memasukkan nama aplikasi untuk mencari aplikasi serupa. Proses ini meliputi validasi aplikasi, perhitungan jarak untuk menemukan lima aplikasi terdekat, serta penghitungan rata-rata Sentiment Polarity dan Sentiment Subjectivity untuk setiap aplikasi mirip. Hasil rekomendasi disusun dalam tabel, diurutkan berdasarkan Sentiment Polarity, sehingga pengguna dapat dengan mudah menemukan aplikasi yang relevan. Jumlah yang direkomendasikan sebagai top n yaitu 5, dapat dilihat seperti dibawah ini:

Sentiment Polarity rata-rata dari aplikasi 'Blogger': 0.1187
Sentiment Subjectivity rata-rata dari aplikasi 'Blogger': 0.5304

Rekomendasi aplikasi yang mirip dengan 'Blogger':

| Aplikasi                     | Sentiment Polarity | Sentiment Subjectivity |
|-------------------------------|-------------------|-----------------------|
| AMC Theatres                  |            0.1378 |                0.6063 |
| Banorte Movil                 |            0.1363 |                0.6059 |
| Chapters: Interactive Stories |            0.1105 |                0.5013 |
| Cool Reader                   |            0.1091 |                0.4825 |
| Baby Panda’s Juice Shop       |            0.1083 |                0.4917 |



## Evaluation

### 1. Content-Based Filtering
Saya menggunakan metrik precision untuk mengukur kinerja model pada content-based filtering. precision adalah metrik yang menilai seberapa baik model dalam memberikan prediksi atau rekomendasi yang bersifat positif benar (true positive) dibandingkan positif salah (false positive). Ketika suatu data diklasifikasikan sebagai positif, metrik ini akan menilai seberapa presisi model dalam memprediksi atau memberi rekomendasi data yang diklasifikasikan positif tersebut. 
   ![precision](https://miro.medium.com/v2/resize:fit:700/1*pDx6oWDXDGBkjnkRoJS6JA.png) <br>
Dihitung dengan membagi true_positives dengan jumlah total aplikasi yang direkomendasikan (len(recommended_apks)). Jika tidak ada rekomendasi, precision disetel ke 0 untuk menghindari pembagian dengan nol. Pada program saya, precision menunjukkan 1.00, yang berarti semua rekomendasi yang diberikan oleh model adalah benar-benar positif. Dalam konteks ini, model berhasil merekomendasikan aplikasi-aplikasi yang memiliki sentimen positif tanpa menghasilkan rekomendasi yang salah. Ini menunjukkan bahwa model sangat efektif dalam mengidentifikasi aplikasi yang relevan berdasarkan kriteria sentiment yang telah ditetapkan.

### 2. Collaborative Filtering
Saya menggunakan Root Mean Squared Error (RMSE) untuk mengukur kinerja model pada collaborativve filtering. RMSE adalah metrik yang digunakan untuk menilai seberapa akurat hasil prediksi atau rekomendasi dibandingkan dengan nilai sebenarnya. Nilai RMSE yang lebih kecil menunjukkan bahwa kesalahan dalam prediksi atau rekomendasi model juga lebih kecil. RMSE dihitung dengan cara mengkuadratkan selisih antara nilai prediksi dan nilai aktual, kemudian menjumlahkan semua kesalahan kuadrat tersebut, membaginya dengan jumlah data, dan terakhir mengambil akar dari hasil tersebut agar satuannya sama dengan satuan nilai aslinya.
![precision](https://media.geeksforgeeks.org/wp-content/uploads/20200622171741/RMSE1.jpg) <br>
Dalam program ini, saya menghitung RMSE untuk nilai Sentiment_Polarity dari model prediksi yang dibangun. Hasil perhitungan yang diperoleh adalah: `0.3315518816226507`. Nilai RMSE sebesar 0.3316 menunjukkan bahwa model memiliki kesalahan prediksi rata-rata yang cukup kecil dalam memprediksi polaritas sentimen. Hal ini menandakan bahwa model tersebut cukup akurat dalam merekomendasikan aplikasi berdasarkan sentimen yang dianalisis.

## Kesimpulan 
Model content-based filtering dan collaborative filtering yang telah dibangun telah berhasil menjawab permasalahan yang diajukan dan mencapai tujuan yang ditetapkan. Kedua model ini memberikan kontribusi signifikan dalam meningkatkan kualitas rekomendasi aplikasi di Play Store. Namun, masih terdapat ruang untuk pengembangan lebih lanjut seperti gabungan dari 2 model (Hibryd Filtering) agar model rekomendasi dapat memberikan hasil yang lebih baik dan lebih relevan dengan kebutuhan pengguna.

## Referensi
[1] Bhineka, "AI turut berpartisipasi pada rekomendasi di Play Store", Retrieved from: https://www.bhinneka.com/blog/ai-turut-berpartisipasi-pada-rekomendasi-di-play-store/
[2] Jacob Murel Ph.D., Eda Kavlakoglu, "What is content-based filtering?", Retrieved from: https://www.ibm.com/topics/content-based-filtering?form=MG0AV3
[3] Aman Kharwal, "Content Based Filtering and Collaborative Filtering: Difference", Retrieved from: https://thecleverprogrammer.com/2023/04/20/content-based-filtering-and-collaborative-filtering-difference/
[4] developers.google.com, "Collaborative filtering", Retrieved from: https://developers.google.com/machine-learning/recommendation/collaborative/basics?hl=id


