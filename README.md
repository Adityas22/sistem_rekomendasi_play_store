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
  Collaborative Filtering (CF) menggunakan data interaksi pengguna lain yang memiliki preferensi serupa untuk merekomendasikan item[[4]](https://www.ibm.com/topics/collaborative-filtering?form=MG0AV3). Kelebihan CF adalah kemampuannya untuk merekomendasikan item yang mungkin tidak pernah dipertimbangkan oleh pengguna, karena ia memanfaatkan informasi dari komunitas pengguna secara keseluruhan. Namun, kelemahannya termasuk masalah cold-start bagi pengguna baru atau item baru, serta ketergantungan pada data interaksi yang cukup untuk menghasilkan rekomendasi yang akurat[[5]](https://developers.google.com/machine-learning/recommendation/collaborative/basics?hl=id).

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

Pada Dataset ini terdapat 2 berkas csv diantaranya yaitu `googleplaystore.csv`  dan `googleplaystore_user_reviews.csv`

Pada berkas `googleplaystore.csv` memuat data-data buku yang terdiri dari 10.841  baris dan memiliki 13  kolom, diantaranya adalah :
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

Pada berkas `googleplaystore_user_reviews.csv` memuat data-data buku yang terdiri dari 64.295   baris dan memiliki 5  kolom, diantaranya adalah :
- App : 	Name of app
- Translated Reviews : 	User review (Preprocessed and translated to English)
- Sentiment : Positive/Negative/Neutral (Preprocessed)
- Sentiment_polarity :	Sentiment polarity score
- Sentiment_subjectivity :	Sentiment subjectivity score

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
- Memeriksa apakah ada nilai hilang dalam dataset all_apk_user. Nilai hilang dapat memengaruhi hasil analisis kita, jadi kita perlu menanganinya dengan tepat. Sekarang disimpan pada variable `all_apk_user_cleaned`

| Kolom                  | Missing Value |
|-----------------------|---------------|
| App                   | 0             |
| Translated_Review     | 51298         |
| Sentiment             | 51288         |
| Sentiment_Polarity    | 51288         |
| Sentiment_Subjectivity | 51288         |
| Category              | 2739          |
| Rating                | 2779          |
| Genres                | 2739          |

- Karena setiap aplikasi seharusnya hanya muncul sekali dalam dataset kita, kita perlu memeriksa dan menghapus entri duplikat berdasarkan kolom App. Ini memastikan bahwa dataset kita tetap bersih dan akurat. Sekarang disimpan pada variable `preparation`.
- Setelah memastikan bahwa dataset kita bersih dari nilai hilang dan duplikat, kita dapat mengonversi kolom tertentu menjadi list. Misalnya, kita bisa mengonversi kolom Genres dan Rating menjadi list untuk memudahkan pemrosesan selanjutnya.
- Setelah mengonversi data menjadi list, kita dapat membuat dictionary untuk menyimpan pasangan key-value. Dictionary ini bisa digunakan untuk menyimpan informasi penting, seperti mengaitkan setiap aplikasi dengan genre dan Rating-nya.

### 2. Collaborative Filtering
- Dataset yang dipakai adalah `googleplaystore_user_reviews.csv`, kemudian memeriksa apakah ada nilai hilang dalam dataset tersebut.  Nilai hilang dapat memengaruhi hasil analisis kita, jadi kita perlu menanganinya dengan tepat. Sekarang disimpan pada variable `user_clean`
  
| Kolom                  | Missing Value |
|-----------------------|---------------|
| App                   | 0             |
| Translated_Review     | 26868         |
| Sentiment             | 26863         |
| Sentiment_Polarity    | 26863         |
| Sentiment_Subjectivity | 26863         |

- Setelah membersihkan dataset dari nilai hilang, langkah selanjutnya adalah membagi dataset `user_clean` menjadi dua subset: 80% untuk pelatihan (training) dan 20% untuk pengujian (testing). Pembagian ini penting untuk memastikan bahwa model yang kita latih tidak terpapar pada data yang sama ketika kita mengujinya.

## Modeling and Result
Berdasarkan pernyataaan solusi sebelumnya, proses pemodelan dibagi menjadi dua metode pendekatan, yaitu metode content-based filtering dan metode collaborative filtering. Berikut adalah penjelasan dan tahapan dalam proses pemodelan dari masing-masing metode pendekatan.
### 1. Content-Based Filtering
Proses dimulai dengan TfidfVectorizer dari sklearn yang digunakan untuk mengekstrak fitur dari kolom Genres dengan menghitung Term Frequency-Inverse Document Frequency (TF-IDF), yang mengubah teks menjadi representasi numerik. Proses ini melibatkan fitting model pada data genre untuk menghitung nilai IDF dan kemudian mentransformasikannya menjadi matriks TF-IDF `(Dalam hal ini ukuran matriks 816 X 61)`. Matriks ini menunjukkan bobot setiap kata dalam genre untuk setiap aplikasi dan disimpan dalam sebuah DataFrame untuk analisis lebih lanjut. <br>
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
Setelah itu, cosine similarity dihitung untuk mengukur seberapa mirip dua aplikasi berdasarkan vektor TF-IDF mereka, dengan nilai berkisar antara 0 (tidak mirip) hingga 1 (sangat mirip). Matriks cosine similarity disusun dalam DataFrame, memudahkan visualisasi aplikasi yang mirip satu sama lain. Fungsi `apk_recommendations_based` kemudian diimplementasikan untuk memberikan rekomendasi berdasarkan nama aplikasi yang dimasukkan pengguna, mencari aplikasi mirip melalui nilai cosine similarity, dan menghapus aplikasi yang sama dari daftar rekomendasi. Rekomendasi ini diurutkan berdasarkan rating, dan sejumlah aplikasi ditampilkan sesuai parameter yang ditentukan `(n=10)`.<br>
Hasil dari proses ini pengguna memasukkan nama aplikasi dan menerima rekomendasi aplikasi lainnya yang memiliki kesamaan genre dan rating yang tinggi, dapat dilihat seperti dibawah ini: 
  ````
Rekomendasi untuk APK '1800 Contacts - Lens Store':
                                      App  Genres  Rating  Sentiment_Polarity  Sentiment_Subjectivity Sentiment
                  Ada - Your Health Guide Medical     4.7            0.377083                0.683333  Positive
           BELONG Beating Cancer Together Medical     4.7            1.000000                0.750000  Positive
           Baritastic - Bariatric Tracker Medical     4.7            0.541667                0.916667  Positive
                     All Mental disorders Medical     4.5           -0.277588                0.766667  Negative
              Anatomy Learning - 3D Atlas Medical     4.5            0.362500                0.500000  Positive
Airway Ex - Intubate. Anesthetize. Train. Medical     4.3            0.150000                0.875000  Positive
              Banfield Pet Health Tracker Medical     4.2            0.061905                0.528571  Positive
                  BioLife Plasma Services Medical     3.5           -0.060000                0.490000  Negative
                          Anthem Anywhere Medical     2.7           -0.275000                0.483333  Negative
                       Anthem BC Anywhere Medical     2.6            0.158333                0.295833  Positive

  ````
### 2. Collaborative Filtering
Dataset yang sudah dibagi menjadi dua bagian: train set dan test set pada data preparation kemudian dibuat pivot table yang menyusun data menjadi matriks di mana baris mewakili aplikasi dan kolom mewakili nilai sentimen, memungkinkan perhitungan rata-rata nilai sentimen untuk setiap aplikasi. Model K-Nearest Neighbors (KNN) digunakan untuk menemukan aplikasi yang mirip berdasarkan nilai sentimen, dengan metrik cosine untuk mengukur kemiripan antara aplikasi. Sebuah fungsi `find_similar_items_knn` diciptakan untuk mencari aplikasi mirip, menerima nama aplikasi sebagai input, menemukan indeks aplikasi dalam matriks, dan menggunakan model KNN untuk mencari aplikasi terdekat. Pengguna diminta untuk memasukkan nama aplikasi yang diinginkan, dan rata-rata polaritas serta subjektivitas dari aplikasi tersebut dihitung dan ditampilkan.<br>
Hasil dari proses ini pengguna memasukkan nama aplikasi,  Untuk setiap aplikasi yang direkomendasikan, rata-rata polaritas dan subjektivitas dihitung dan disimpan dalam sebuah list. Data rekomendasi kemudian diurutkan berdasarkan nilai Sentiment Polarity dari tertinggi ke terendah, dapat dilihat seperti dibawah ini: <br>
````
Sentiment Polarity rata-rata dari aplikasi '1800 Contacts - Lens Store': 0.3284
Sentiment Subjectivity rata-rata dari aplikasi '1800 Contacts - Lens Store': 0.5792

Rekomendasi aplikasi yang mirip dengan '1800 Contacts - Lens Store':
                                  Aplikasi  Sentiment Polarity  Sentiment Subjectivity
       2Date Dating App, Love and matching            0.325684                0.574011
                            GRE Flashcards            0.319495                0.565242
30 Day Fitness Challenge - Workout at Home            0.308258                0.543605
                        Google My Business            0.262570                0.464485
            Digit Save Money Automatically            0.220794                0.389645
````

## Evaluation

### 1. Content-Based Filtering
Saya menggunakan metrik precision untuk mengukur kinerja model pada content-based filtering. precision adalah metrik yang menilai seberapa baik model dalam memberikan prediksi atau rekomendasi yang bersifat positif benar (true positive) dibandingkan positif salah (false positive). Ketika suatu data diklasifikasikan sebagai positif, metrik ini akan menilai seberapa presisi model dalam memprediksi atau memberi rekomendasi data yang diklasifikasikan positif tersebut. 
