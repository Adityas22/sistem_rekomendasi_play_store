#!/usr/bin/env python
# coding: utf-8

# System recommendation aplikasi play store

# Oleh : Aditya Septiawan
# 
# dataset : https://www.kaggle.com/datasets/whenamancodes/play-store-apps

# ## Data Understanding
# 

# memahami cakupan dan jumlah data unik yang ada dalam kedua dataset

# In[1]:


import pandas as pd

user = pd.read_csv('dataset-play-store/googleplaystore_user_reviews.csv')
apk = pd.read_csv('dataset-play-store/googleplaystore.csv')
 
print('Jumlah data pada play store: ', len(apk.App.unique()))
print('Jumlah data pada user review: ', len(user.App.unique()))



# ## Univariate Exploratory Data Analysis

# menampilkan ringkasan informasi dari dataframe user

# In[2]:


user.info()


# menampilkan statistik deskriptif pada kolom numerik dari user

# In[3]:


# Tampilkan deskripsi 
user.describe()


# menghitung jumlah nilai kosong (null) di setiap kolom pada user

# In[4]:


user.isnull().sum()


# menampilkan distribusi Sentiment Polarity pada user

# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns

# Set the plot style
sns.set_style("white")

# Plot distribusi Sentiment Polarity
plt.figure(figsize=(12, 6))

# Subplot untuk Sentiment Polarity
plt.subplot(1, 2, 1)
sns.histplot(user['Sentiment_Polarity'].dropna(), kde=True, bins=20, color='blue')
plt.title('Distribution of Sentiment Polarity')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Frequency')
plt.show()


# menampilkan distribusi Sentiment Subjectivity pada user

# In[6]:


# Subplot untuk Sentiment Subjectivity
plt.subplot(1, 2, 2)
sns.histplot(user['Sentiment_Subjectivity'].dropna(), kde=True, bins=20, color='green')
plt.title('Distribution of Sentiment Subjectivity')
plt.xlabel('Sentiment Subjectivity')
plt.ylabel('Frequency')

# Menampilkan plot
plt.tight_layout()
plt.show()


# memberikan ringkasan informasi pada apk

# In[7]:


apk.info()


# mengubah semua spasi di nama kolom menjadi underscore _

# In[8]:


apk.columns = apk.columns.str.replace(' ', '_')


# menampilkan statistik deskriptif pada kolom numerik dari user

# In[9]:


apk.describe()


# menampilkan distribusi Rating pada apk

# In[10]:


plt.figure(figsize=(18, 14))
plt.subplot(3, 1, 2)
sns.histplot(apk['Rating'].dropna(), kde=True, bins=20, color='orange')
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')

# Tampilkan plot
plt.show()


# menampilkan distribusi Genres pada user

# In[11]:


plt.figure(figsize=(18, 14))
plt.subplot(3, 1, 3)
genres_counts = apk['Genres'].value_counts().head(20)  # Menampilkan 20 genre teratas
sns.barplot(x=genres_counts.index, y=genres_counts.values, palette="magma")
plt.title('Top 20 Genres Distribution')
plt.xlabel('Genres')
plt.ylabel('Count')
plt.xticks(rotation=90)

# Tampilkan plot
plt.tight_layout()
plt.show()


# ## Data Preparation untuk CBF

# Menghapus kolom tertentu untuk menyederhanakan dan hanya dengan kolom-kolom yang relevan bagi analisis

# In[12]:


apk = apk.drop(columns=['Reviews', 'Size', 'Price', 'Type', 'Installs', 'Content_Rating', 'Last_Updated', 'Current_Ver', 'Android_Ver'], axis=1)
apk


# menggabungkan dua DataFrame, yaitu user dan apk  untuk mengaitkan informasi ulasan pengguna dengan data aplikasi

# In[13]:


all_apk_user = pd.merge(user,  apk, on='App', how='left')
all_apk_user


# menghitung jumlah nilai kosong (null) pada all_apk_user dimana pada dataset yang sudah digabung sebelumnya

# In[14]:


all_apk_user.isnull().sum()


# menghapus semua baris yang memiliki nilai kosong (null) 

# In[15]:


all_apk_user_cleaned = all_apk_user.dropna()


# menghapus duplikasi berdasarkan kolom App untuk memastikan bahwa analisis berikutnya tidak akan terpengaruh oleh adanya aplikasi yang sama lebih dari sekali,

# In[16]:


preparation = all_apk_user_cleaned.drop_duplicates('App')
preparation


#  mengonversi kolom dari DataFrame preparation menjadi list kemudian mencetak panjang (len) masing-masing list tersebut untuk verifikasi

# In[17]:


# Mengonversi kolom 'App' menjadi list
app_list = preparation['App'].tolist()

# Mengonversi kolom 'Translated_Review' menjadi list
translated_review_list = preparation['Translated_Review'].tolist()

# Mengonversi kolom 'Sentiment' menjadi list
sentiment_list = preparation['Sentiment'].tolist()

# Mengonversi kolom 'Sentiment_Polarity' menjadi list
sentiment_polarity_list = preparation['Sentiment_Polarity'].tolist()

# Mengonversi kolom 'Sentiment_Subjectivity' menjadi list
sentiment_subjectivity_list = preparation['Sentiment_Subjectivity'].tolist()

# Mengonversi kolom 'Category' menjadi list
category_list = preparation['Category'].tolist()

# Mengonversi kolom 'Rating' menjadi list
rating_list = preparation['Rating'].tolist()

# Mengonversi kolom 'Genres' menjadi list
genres_list = preparation['Genres'].tolist()

# Cetak panjang dari masing-masing list untuk verifikasi
print(len(app_list))
print(len(translated_review_list))
print(len(sentiment_list))
print(len(sentiment_polarity_list))
print(len(sentiment_subjectivity_list))
print(len(category_list))
print(len(rating_list))
print(len(genres_list))


# membuat DataFrame baru dari kolom-kolom yang telah dikonversi menjadi list sebelumnya. menghasilkan struktur data yang terorganisir dengan baik, di mana setiap kolom mewakili informasi yang relevan tentang aplikasi dan ulasan pengguna

# In[18]:


# Membuat dictionary baru dari kolom yang digunakan
apk_user_dict = pd.DataFrame({
    'App': app_list,                                 # Nama aplikasi
    'Translated_Review': translated_review_list,     # Ulasan yang telah diterjemahkan
    'Sentiment': sentiment_list,                     # Sentimen ulasan (Positif/Negatif/Netral)
    'Sentiment_Polarity': sentiment_polarity_list,   # Polaritas sentimen
    'Sentiment_Subjectivity': sentiment_subjectivity_list,  # Subjektivitas sentimen
    'Category': category_list,                       # Kategori aplikasi
    'Rating': rating_list,                           # Rating aplikasi
    'Genres': genres_list                            # Genre aplikasi
})

apk_user_dict


# menghitung dan memetakan fitur dari kolom Genres dalam DataFrame apk_user_dict menggunakan metode TF-IDF. TF-IDF membantu dalam mengidentifikasi seberapa penting suatu kata dalam koleksi dokumen. 

# In[19]:


from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tfidf_vectorizer  = TfidfVectorizer()
 
# Melakukan perhitungan idf pada data 'Genres'
tfidf_vectorizer.fit(apk_user_dict['Genres']) 
 
# Mapping array dari fitur index integer ke fitur nama
tfidf_vectorizer.get_feature_names_out() 


# ## Model Development dengan Content Based Filtering

# melakukan transformasi data kolom Genres menjadi matriks TF-IDF dan memeriksa ukuran matriks tersebut untuk memahami dimensi dari data yang telah diproses, serta untuk memastikan bahwa transformasi berhasil dan matriks memiliki ukuran yang sesuai untuk analisis atau pemodelan selanjutnya.

# In[20]:


# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(apk_user_dict['Genres']) 
 
# Melihat ukuran matrix tfidf
tfidf_matrix.shape


# mengubah matriks TF-IDF yang awalnya dalam bentuk sparse menjadi bentuk dense untuk melakukan analisis lebih lanjut atau memvisualisasikan data

# In[21]:


# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix_dense = tfidf_matrix.todense()
tfidf_matrix_dense


# membuat DataFrame dari matriks TF-IDF yang telah diubah menjadi bentuk dense, sehingga memungkinkan untuk melihat nilai-nilai TF-IDF dengan lebih mudah, memvisualisasikan dan menganalisis data TF-IDF dengan cara yang lebih terstruktur.

# In[22]:


# Membuat dataframe untuk melihat tf-idf matrix

# Membuat DataFrame untuk melihat tf-idf matrix
tfidf_df = pd.DataFrame(
    tfidf_matrix_dense, 
    columns=tfidf_vectorizer.get_feature_names_out(), 
    index=apk_user_dict['Genres'],
)

# Tampilkan matriks tf-idf
tfidf_df.sample(22, axis=1).sample(10, axis=0)


# menghitung cosine similarity antara dokumen-dokumen dalam matriks TF-IDF yang telah dibuat.

# Cosine similarity adalah metrik yang umum digunakan dalam analisis teks untuk mengukur seberapa mirip dua teks berdasarkan sudut antara vektor-vektor mereka dalam ruang fitur. 

# In[23]:


# Menghitung cosine similarity pada matrix tf-idf
from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim


# menghitung ulang matriks TF-IDF dan cosine similarity untuk menganalisis kemiripan dokumen dalam konteks subset tertentu dari data

# In[24]:


# Menghitung ulang TF-IDF untuk subset data
tfidf_matrix_subset = tfidf_vectorizer.fit_transform(apk_user_dict['Genres'])

# Menghitung cosine similarity pada subset matrix
cosine_sim_subset = cosine_similarity(tfidf_matrix_subset)

# Menampilkan ukuran matrix cosine similarity
print('Cosine Similarity Matrix Shape:', cosine_sim_subset.shape)


# membuat DataFrame dari matriks cosine similarity yang telah dihitung dan memvisualisasikan hasilnya dengan cara yang lebih terstruktur. 

# In[25]:


# Membuat dataframe dari variabel cosine_sim_subset dengan baris dan kolom dari subset App
cosine_sim_df = pd.DataFrame(cosine_sim_subset, 
                             index=apk_user_dict['App'], 
                             columns=apk_user_dict['App'])

# Menampilkan ukuran matrix
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix secara acak untuk 7 kolom dan 10 baris
cosine_sim_df.sample(7, axis=1).sample(10, axis=0)


# memberikan rekomendasi aplikasi berdasarkan kemiripan cosine antara aplikasi yang diberikan.

# In[26]:


def apk_recommendations_based(name_apk, similarity_data=cosine_sim_df, items=apk_user_dict[['App', 'Genres', 'Rating', 'Sentiment_Polarity', 'Sentiment_Subjectivity', 'Sentiment']], n=10):
    # Mencari index game yang mirip berdasarkan cosine similarity
    similar_apk = similarity_data[name_apk].nlargest(n + 1).index
    
    # Drop game yang sama dari daftar rekomendasi
    similar_apk = similar_apk.drop(name_apk, errors='ignore')

    # Mengambil data rekomendasi
    recommendations = items[items['App'].isin(similar_apk)]
    
    # Mengurutkan berdasarkan Rating
    recommendations = recommendations.sort_values(by='Rating', ascending=False)
    
    return recommendations.head(n)


# mengambil input dari pengguna dan kemudian menggunakan fungsi apk_recommendations_based untuk memberikan rekomendasi aplikasi berdasarkan input tersebut.

# In[28]:


from tabulate import tabulate

# Mengambil input dari user
name_apk_input = input("Masukkan nama APK yang ingin direkomendasikan: ")
recommendations = apk_recommendations_based(name_apk_input)

# Menampilkan hasil dengan input di bagian atas
print(f"\nRekomendasi untuk APK '{name_apk_input}':")
print(tabulate(recommendations, headers='keys', tablefmt='github', showindex=False))


# menghitung dan menampilkan nilai precision dari rekomendasi aplikasi berdasarkan sentimen positif

# In[29]:


# Mendefinisikan aplikasi relevan (ground truth) sebagai aplikasi dengan Sentiment positif
relevant_apks = set(preparation['App'])

# Mendapatkan nama aplikasi yang direkomendasikan dalam bentuk set
recommended_apks = set(recommendations['App'])

# Menghitung Precision dan Recall
true_positives = len(recommended_apks.intersection(relevant_apks))
precision = true_positives / len(recommended_apks) if recommended_apks else 0

print(f"\nPrecision: {precision:.2f}")


# ## Model Development dengan Collaborative Filtering

# ### Data Preparation (dataset yang dipakai hanya user review)

# menampilkan ringkasan informasi  dari user

# In[30]:


user.info()


# menghitung jumlah nilai kosong (null) di setiap kolom pada user

# In[31]:


user.isnull().sum()


# menghapus semua baris dalam yang memiliki nilai NaN

# In[32]:


user_clean = user.dropna()


# In[33]:


user_clean


#  membagi dataset ulasan aplikasi yang telah dibersihkan menjadi train set dan test set (80:20), Mengubah train_data menjadi tabel pivot kemudian kolom yang akan dihitung adalah Sentiment_Polarity dan Sentiment_Subjectivity.

# In[34]:


from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Pisahkan dataset menjadi train dan test set
train_data, test_data = train_test_split(user_clean, test_size=0.2, random_state=42)

# Buat pivot table dari train_data untuk membentuk matriks item similarity berdasarkan Sentiment_Polarity 
item_matrix_train = train_data.pivot_table(index='App', values=['Sentiment_Polarity', 'Sentiment_Subjectivity'], aggfunc='mean')



# ### Modeling CF

# Membangun model K-Nearest Neighbors (KNN) untuk menemukan aplikasi yang mirip

# In[35]:


# Menggunakan K-Nearest Neighbors untuk mencari kemiripan antar aplikasi
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(item_matrix_train)


# memberikan rekomendasi aplikasi yang mirip berdasarkan model K-Nearest Neighbors dengan jumlah yang direkomendasikan yaitu 5

# In[36]:


# Fungsi untuk mencari aplikasi mirip
def find_similar_items_knn(app_name, item_matrix_train, model, n=5):
    if app_name in item_matrix_train.index:
        # Mendapatkan indeks aplikasi yang diberikan
        idx = item_matrix_train.index.get_loc(app_name)
        distances, indices = model.kneighbors(item_matrix_train.iloc[idx, :].values.reshape(1, -1), n_neighbors=n+1)
        
        # Ambil hasil dalam bentuk DataFrame untuk aplikasi yang mirip
        similar_apps = pd.DataFrame({
            'Aplikasi': item_matrix_train.index[indices.flatten()],
            'Jarak': distances.flatten()
        }).sort_values(by='Jarak').iloc[1:]  # Hilangkan aplikasi itu sendiri dari hasil
        
        return similar_apps
    else:
        raise ValueError(f"Aplikasi '{app_name}' tidak ditemukan dalam data.")


# menganalisis sentimen aplikasi berdasarkan input dari pengguna

# List rekomendasi diurutkan berdasarkan Sentiment_Polarity dari yang tertinggi ke terendah

# In[44]:


# Input aplikasi dari pengguna
app_input = input("Masukkan nama aplikasi: ")

try:
    # Menampilkan Sentiment Polarity dan Subjectivity rata-rata dari aplikasi yang dimasukkan pengguna
    user_app_polarity = train_data[train_data['App'] == app_input]['Sentiment_Polarity'].mean()
    user_app_subjectivity = train_data[train_data['App'] == app_input]['Sentiment_Subjectivity'].mean()
    
    if pd.isna(user_app_polarity) or pd.isna(user_app_subjectivity):
        raise ValueError(f"Aplikasi '{app_input}' tidak ditemukan dalam data pelatihan.")
    
    # Tampilkan Sentiment Polarity dan Subjectivity dari aplikasi input
    print(f"\nSentiment Polarity rata-rata dari aplikasi '{app_input}': {user_app_polarity:.4f}")
    print(f"Sentiment Subjectivity rata-rata dari aplikasi '{app_input}': {user_app_subjectivity:.4f}")
    
    # Cari aplikasi yang mirip dengan KNN
    recommendations = find_similar_items_knn(app_input, item_matrix_train, knn)
    
    # List untuk menyimpan data aplikasi dan rata-rata sentimen
    app_data = []
    
    print(f"\nRekomendasi aplikasi yang mirip dengan '{app_input}':")
    
    for _, row in recommendations.iterrows():
        app_name = row['Aplikasi']
        avg_polarity = train_data[train_data['App'] == app_name]['Sentiment_Polarity'].mean()
        avg_subjectivity = train_data[train_data['App'] == app_name]['Sentiment_Subjectivity'].mean()
        
        # Tambahkan data aplikasi ke dalam list
        app_data.append([app_name, avg_polarity, avg_subjectivity])
    
    # Urutkan aplikasi berdasarkan Sentiment Polarity dari tertinggi ke terendah
    app_data_sorted = sorted(app_data, key=lambda x: x[1], reverse=True)

   # Menghitung panjang maksimum nama aplikasi
    max_app_length = max(len(row['Aplikasi']) for _, row in recommendations.iterrows())
    # Tambahkan padding jika perlu
    max_app_length = max(max_app_length, 27)  # Set minimal lebar 27 jika lebih kecil

    # Menampilkan hasil dalam format tabel Markdown
    print("\n| Aplikasi" + " " * (max_app_length - 8) + "| Sentiment Polarity | Sentiment Subjectivity |")
    print("|" + "-" * (max_app_length + 2) + "|-------------------|-----------------------|")
    for app_name, polarity, subjectivity in app_data_sorted:
        print(f"| {app_name:<{max_app_length}} | {polarity:>17.4f} | {subjectivity:>21.4f} |")
        
except ValueError as e:
    print(e)


# memprediksi nilai sentimen rata-rata (polarity dan subjectivity) dari aplikasi menggunakan algoritma K-Nearest Neighbors (KNN) dan kemudian menghitung error metrik dengan Root Mean Squared Error (RMSE) 

# In[38]:


from sklearn.metrics import mean_squared_error

# Fungsi untuk menemukan aplikasi mirip dan memprediksi sentimen rata-rata
def predict_sentiment_knn(app_name, item_matrix_train, model, train_data, n=5):
    if app_name in item_matrix_train.index:
        # Cari n aplikasi mirip
        idx = item_matrix_train.index.get_loc(app_name)
        distances, indices = model.kneighbors(item_matrix_train.iloc[idx, :].values.reshape(1, -1), n_neighbors=n+1)
        
        # Ambil aplikasi yang mirip dan hitung rata-rata polarity dan subjectivity
        similar_apps = item_matrix_train.index[indices.flatten()[1:]]  # Hilangkan aplikasi itu sendiri dari hasil
        pred_polarity = train_data[train_data['App'].isin(similar_apps)]['Sentiment_Polarity'].mean()
        pred_subjectivity = train_data[train_data['App'].isin(similar_apps)]['Sentiment_Subjectivity'].mean()
        
        return pred_polarity, pred_subjectivity
    else:
        # Jika tidak ada aplikasi yang mirip, gunakan default (misalnya 0)
        return 0, 0

# Menghitung nilai sebenarnya dari test set
y_true_polarity = test_data['Sentiment_Polarity'].values

# Prediksi polarity dan subjectivity pada test set
y_pred_polarity = []

for app in test_data['App']:
    pred_polarity, pred_subjectivity = predict_sentiment_knn(app, item_matrix_train, knn, train_data)
    y_pred_polarity.append(pred_polarity)

# Menghitung Root Mean Squared Error (RMSE) dan Mean Absolute Error (MAE) untuk Sentiment_Polarity
rmse_polarity = mean_squared_error(y_true_polarity, y_pred_polarity, squared=False)


print(f"Root Mean Squared Error (Polarity): {rmse_polarity}")

