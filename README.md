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
   ![Rating](https://github.com/Adityas22/sistem_rekomendasi_play_store/blob/main/image/Rating.png)
   Visualisasi data rating ini cenderung mendapatkan penilaian yang tinggi dari pengguna, dengan puncak frekuensi pada rating 5.0. Namun, grafik juga menunjukkan adanya sebaran rating yang cukup luas, dengan frekuensi yang signifikan pada rating 4.5, 4.0, dan 3.5, mengindikasikan bahwa pengguna memberikan penilaian yang beragam.
2. Genre
   ![Genre](https://github.com/Adityas22/sistem_rekomendasi_play_store/blob/main/image/Genres.png)
   Visualisasi data genre ini terlihat bahwa aplikasi di platform ini didominasi oleh kategori "Tools" atau utilitas, yang menunjukkan jumlah jauh lebih besar dibandingkan genre lainnya. Namun, terdapat pula beberapa genre dengan distribusi yang cukup merata, seperti "Entertainment", "Education", dan "Medical", menandakan keberagaman preferensi pengguna. Di sisi lain, ada beberapa genre niche atau khusus, seperti "Travel & Local", "Sports", dan "Dating", yang mengindikasikan adanya segmentasi pasar yang perlu dipertimbangkan. Selain itu, terdapat peluang pengembangan di genre-genre yang saat ini kurang terwakili, seperti "News & Magazines" dan "Books & Reference".

Berikut ini adalah hasil dari visualiasi `googleplaystore_user_reviews.csv`.
1. Sentiment_polarity <br>
   ![Sentiment_polarity](https://github.com/Adityas22/sistem_rekomendasi_play_store/blob/main/image/sentiment_polarity.png) <br>
   Visualisasi data Sentiment_polarity menunjukkan bahwa mayoritas ulasan atau sentimen yang diberikan pengguna cenderung berada pada posisi netral, dengan puncak frekuensi yang dominan pada polaritas 0.00.
3. Sentiment_subjectivity <br>
   ![Sentiment_subjectivity](https://github.com/Adityas22/sistem_rekomendasi_play_store/blob/main/image/Sentiment_Subjectivity.png) <br>
   Visualisasi data Sentiment_subjectivity ini Terlihat puncak yang dominan pada nilai subjektivitas 0.8, mengindikasikan bahwa sebagian besar ulasan atau sentimen yang diberikan pengguna cenderung bersifat sangat subjektif.
