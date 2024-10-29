#!/usr/bin/env python
# coding: utf-8

# System recommendation aplikasi play store

# Oleh : Aditya Septiawan
# 
# dataset : https://www.kaggle.com/datasets/whenamancodes/play-store-apps

# ## Data Understanding
# 

# In[1]:


import pandas as pd

user = pd.read_csv('dataset-play-store/googleplaystore_user_reviews.csv')
apk = pd.read_csv('dataset-play-store\googleplaystore.csv')
 
print('Jumlah data pada play store: ', len(apk.App.unique()))
print('Jumlah data pada user review: ', len(user.App.unique()))



# ## Univariate Exploratory Data Analysis

# User Variabel

# In[2]:


user.info()


# melihat data

# In[3]:


print('Banyak data: ', len(user.App.unique()))
print('Translated_Review: ', user.Translated_Review.unique())
print('Sentiment: ', user.Sentiment.unique())
print('Sentiment_Polarity: ', user.Sentiment_Polarity.unique())
print('Sentiment_Subjectivity: ', user.Sentiment_Subjectivity.unique())


# cek nilai

# In[4]:


# Tampilkan deskripsi 
user.describe()


# visual Sentiment_Polarity

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


# visual Sentiment_Subjectivity

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


# Aplikasi play store Variabel

# In[7]:


apk.columns = apk.columns.str.replace(' ', '_')
apk.info()


# melihat data

# In[8]:


print('Banyak data: ', len(apk.App.unique()))
print('Category: ', apk.Category.unique())
print('Content Rating: ', apk.Content_Rating  .unique())
print('Genres: ', apk.Genres.unique())
print('Rating: ', apk.Rating.unique())


# cek nilai

# In[9]:


apk.describe()


# visual category

# In[10]:


plt.figure(figsize=(18, 14))
plt.subplot(3, 1, 1)
category_counts = apk['Category'].value_counts()
sns.barplot(x=category_counts.index, y=category_counts.values, palette="viridis")
plt.title('Distribution of Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=90)

plt.show()


# visual rating

# In[11]:


plt.figure(figsize=(18, 14))
plt.subplot(3, 1, 2)
sns.histplot(apk['Rating'].dropna(), kde=True, bins=20, color='orange')
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')

# Tampilkan plot
plt.show()


# visual genre

# In[12]:


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


# ## Data Preprocessing

# menghapus kolom review, size, type, price, Installs, content_rating, Last_Updated, Current_Ver, Android_Ver  pada aplikasi karena tidak terlalu digunakan. berfokus pada category, rating, dan genre

# In[13]:


apk = apk.drop(columns=['Reviews', 'Size', 'Price', 'Type', 'Installs', 'Content_Rating', 'Last_Updated', 'Current_Ver', 'Android_Ver'], axis=1)
apk


# menggabungkan data games dan recommendation

# In[14]:


all_apk_user = pd.merge(user,  apk, on='App', how='left')
all_apk_user


# ## Data Preparation

# mengecek missing value

# In[15]:


all_apk_user.isnull().sum()


#  Menghapus Baris dengan Nilai Null

# In[16]:


all_apk_user_cleaned = all_apk_user.dropna()


# In[17]:


all_apk_user_cleaned.isnull().sum()


# menghapus duplikat

# In[18]:


preparation = all_apk_user_cleaned.drop_duplicates('App')
preparation


# konversi data series menjadi list

# In[19]:


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


#  membuat dictionary untuk menentukan pasangan key-value pada data

# In[20]:


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


# ## Model Development dengan Content Based Filtering

# TF-IDF Vectorizer akan digunakan pada sistem rekomendasi untuk menemukan representasi fitur penting dari setiap kolom game. Kita akan menggunakan fungsi tfidfvectorizer() dari library sklearn

# In[21]:


from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tfidf_vectorizer  = TfidfVectorizer()
 
# Melakukan perhitungan idf pada data 'Genres'
tfidf_vectorizer.fit(apk_user_dict['Genres']) 
 
# Mapping array dari fitur index integer ke fitur nama
tfidf_vectorizer.get_feature_names_out() 


#  lakukan fit dan transformasi ke dalam bentuk matriks

# In[22]:


# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(apk_user_dict['Genres']) 
 
# Melihat ukuran matrix tfidf
tfidf_matrix.shape


# Untuk menghasilkan vektor tf-idf dalam bentuk matriks

# In[23]:


# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix_dense = tfidf_matrix.todense()
tfidf_matrix_dense


# lihat matriks tf-idf

# In[24]:


# Membuat dataframe untuk melihat tf-idf matrix

# Membuat DataFrame untuk melihat tf-idf matrix
tfidf_df = pd.DataFrame(
    tfidf_matrix_dense, 
    columns=tfidf_vectorizer.get_feature_names_out(), 
    index=apk_user_dict['Genres'],
)

# Tampilkan matriks tf-idf
tfidf_df.sample(22, axis=1).sample(10, axis=0)


# Cosine Similarity (menghitung derajat kesamaan), dimana data dikurangin karena terlalu besar (ambil 15000 acak)

# In[25]:


# Menghitung cosine similarity pada matrix tf-idf
from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim


# In[26]:


# Menghitung ulang TF-IDF untuk subset data
tfidf_matrix_subset = tfidf_vectorizer.fit_transform(apk_user_dict['Genres'])

# Menghitung cosine similarity pada subset matrix
cosine_sim_subset = cosine_similarity(tfidf_matrix_subset)

# Menampilkan ukuran matrix cosine similarity
print('Cosine Similarity Matrix Shape:', cosine_sim_subset.shape)


# In[ ]:





# In[27]:


# Membuat dataframe dari variabel cosine_sim_subset dengan baris dan kolom dari subset App
cosine_sim_df = pd.DataFrame(cosine_sim_subset, 
                             index=apk_user_dict['App'], 
                             columns=apk_user_dict['App'])

# Menampilkan ukuran matrix
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix secara acak untuk 7 kolom dan 10 baris
cosine_sim_df.sample(7, axis=1).sample(10, axis=0)


# mendapatkan rekomendasi

# In[28]:


def apk_recommendations_based(name_apk, similarity_data=cosine_sim_df, items=apk_user_dict[['App', 'Genres', 'Rating', 'Sentiment_Subjectivity']], n=10):
    # Mencari index game yang mirip berdasarkan cosine similarity
    similar_apk = similarity_data[name_apk].nlargest(n + 1).index
    
    # Drop game yang sama dari daftar rekomendasi
    similar_apk = similar_apk.drop(name_apk, errors='ignore')

    # Mengambil data rekomendasi
    recommendations = items[items['App'].isin(similar_apk)]
    
    # Mengurutkan berdasarkan Rating
    recommendations = recommendations.sort_values(by='Rating', ascending=False)
    
    return recommendations.head(n)


# Menguji Fungsi Rekomendasi

# In[29]:


# Menampilkan 10 aplikasi secara acak di kolom 'App' untuk dicoba pada pengujiabn
print(preparation['App'].sample(10))


# In[30]:


apk_recommendations_based('Happify')



# ## Model Development dengan Collaborative Filtering

# In[31]:


user.info()


# In[32]:


user


# In[33]:


user.isnull().sum()


# In[34]:


user_clean = user.dropna()


# In[35]:


user_clean.isnull().sum()


# In[36]:


user_clean


# Buat matriks baru yang hanya berisi data numerik

# In[37]:


# Membuat pivot table tanpa kolom string
item_matrix = user_clean.pivot_table(index='App', values=['Sentiment_Polarity', 'Sentiment_Subjectivity'], aggfunc='mean')


# In[38]:


item_matrix


# Menghitung cosine similarity

# In[39]:


from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Menghitung cosine similarity antar aplikasi berdasarkan data numerik
scaler = StandardScaler()
item_matrix_scaled = scaler.fit_transform(item_matrix)


# In[40]:


item_matrix_scaled


# In[41]:


# Hitung cosine similarity berdasarkan data yang sudah di-scaling
item_similarity = cosine_similarity(item_matrix_scaled)
item_similarity_df = pd.DataFrame(item_similarity, index=item_matrix.index, columns=item_matrix.index)


# In[42]:


item_similarity_df


# Visualisasi Matriks Kesamaan

# In[43]:


random_apps = item_similarity_df.sample(n=20, random_state=2)  # Set random_state untuk reproducibility
filtered_similarity_df = item_similarity_df.loc[random_apps.index, random_apps.index]

# Visualisasi matriks kesamaan dengan heatmap
plt.figure(figsize=(20, 10))
sns.heatmap(filtered_similarity_df, cmap='coolwarm', annot=True, fmt=".2f")
plt.title('Cosine Similarity antara 20 Aplikasi Random')
plt.xlabel('Aplikasi')
plt.ylabel('Aplikasi')
plt.show()


# membagi dataset

# In[44]:


from sklearn.model_selection import train_test_split

# Pisahkan dataset menjadi train dan test set
train_data, test_data = train_test_split(user_clean, test_size=0.2, random_state=42)

# Buat pivot table dari train_data untuk membentuk matriks item similarity berdasarkan Sentiment_Polarity 
item_matrix_train = train_data.pivot_table(index='App', values=['Sentiment_Polarity', 'Sentiment_Subjectivity'], aggfunc='mean')

# Menghitung cosine similarity antar aplikasi pada training set
from sklearn.metrics.pairwise import cosine_similarity

item_similarity_train = cosine_similarity(item_matrix_train)
item_similarity_df_train = pd.DataFrame(item_similarity_train, index=item_matrix_train.index, columns=item_matrix_train.index)


# In[45]:


# Fungsi untuk mencari aplikasi mirip
def find_similar_items(app_name, item_similarity_df, n=5):
    if app_name in item_similarity_df.index:
        similar_scores = item_similarity_df[app_name].sort_values(ascending=False)
        return similar_scores.head(n)  # Mengembalikan n aplikasi paling mirip
    else:
        raise ValueError(f"Aplikasi '{app_name}' tidak ditemukan.")


#  Mengukur MSE dan MSA

# In[46]:


# Ambil nilai sebenarnya dari test set (baik Sentiment_Polarity maupun Sentiment_Subjectivity)
y_true_polarity = test_data['Sentiment_Polarity'].values
y_true_subjectivity = test_data['Sentiment_Subjectivity'].values

# Prediksi polarity dan subjectivity berdasarkan aplikasi yang mirip
y_pred_polarity = []
y_pred_subjectivity = []
for app in test_data['App']:
    try:
        # Cari aplikasi yang mirip
        similar_items = find_similar_items(app, item_similarity_df_train)
        
        # Prediksi Sentiment_Polarity dan Sentiment_Subjectivity berdasarkan aplikasi yang mirip
        pred_polarity = train_data[train_data['App'].isin(similar_items.index)]['Sentiment_Polarity'].mean()
        pred_subjectivity = train_data[train_data['App'].isin(similar_items.index)]['Sentiment_Subjectivity'].mean()
        
        y_pred_polarity.append(pred_polarity)
        y_pred_subjectivity.append(pred_subjectivity)
    except ValueError:
        # Jika tidak ada aplikasi mirip, gunakan default (misalnya 0)
        y_pred_polarity.append(0)
        y_pred_subjectivity.append(0)

# Menghitung Mean Squared Error (MSE) dan Mean Absolute Error (MAE) untuk Sentiment_Polarity
from sklearn.metrics import mean_squared_error, mean_absolute_error

mse_polarity = mean_squared_error(y_true_polarity, y_pred_polarity)
mae_polarity = mean_absolute_error(y_true_polarity, y_pred_polarity)

# Menghitung MSE dan MAE untuk Sentiment_Subjectivity
mse_subjectivity = mean_squared_error(y_true_subjectivity, y_pred_subjectivity)
mae_subjectivity = mean_absolute_error(y_true_subjectivity, y_pred_subjectivity)

print(f"Mean Squared Error (Polarity): {mse_polarity}")
print(f"Mean Absolute Error (Polarity): {mae_polarity}")

print(f"Mean Squared Error (Subjectivity): {mse_subjectivity}")
print(f"Mean Absolute Error (Subjectivity): {mae_subjectivity}")


# In[47]:


import pandas as pd

# Cari rekomendasi aplikasi berdasarkan input
app_input = input("Masukkan nama aplikasi: ")

try:
    # Ambil rata-rata Sentiment Polarity dan Subjectivity dari aplikasi input user
    user_app_polarity = train_data[train_data['App'] == app_input]['Sentiment_Polarity'].mean()
    user_app_subjectivity = train_data[train_data['App'] == app_input]['Sentiment_Subjectivity'].mean()
    
    if pd.isna(user_app_polarity) or pd.isna(user_app_subjectivity):
        raise ValueError(f"Aplikasi '{app_input}' tidak ditemukan dalam data pelatihan.")
    
    # Tampilkan Sentiment Polarity dan Subjectivity dari aplikasi input
    print(f"\nSentiment Polarity rata-rata dari aplikasi '{app_input}': {user_app_polarity:.4f}")
    print(f"Sentiment Subjectivity rata-rata dari aplikasi '{app_input}': {user_app_subjectivity:.4f}")
    
    # Cari aplikasi yang mirip berdasarkan input
    recommendations = find_similar_items(app_input, item_similarity_df_train)
    
    # List untuk menyimpan data aplikasi dan rata-rata sentimen
    app_data = []
    
    print(f"\nRekomendasi aplikasi yang mirip dengan '{app_input}':")
    
    for app, score in recommendations.items():
        # Ambil rata-rata Sentiment Polarity dan Subjectivity dari aplikasi yang direkomendasikan
        avg_polarity = train_data[train_data['App'] == app]['Sentiment_Polarity'].mean()
        avg_subjectivity = train_data[train_data['App'] == app]['Sentiment_Subjectivity'].mean()
        
        # Tambahkan data aplikasi ke dalam list
        app_data.append([app, avg_polarity, avg_subjectivity])
    
    # Urutkan aplikasi berdasarkan Sentiment Polarity dari tertinggi ke terendah
    app_data_sorted = sorted(app_data, key=lambda x: x[1], reverse=True)

    # Konversi hasil ke dalam dataframe pandas
    df_recommendations = pd.DataFrame(app_data_sorted, columns=['Aplikasi', 'Sentiment Polarity', 'Sentiment Subjectivity'])

    # Tampilkan hasil dalam bentuk tabel
    print(df_recommendations.to_string(index=False))
        
except ValueError as e:
    print(e)


# ## Hybrid (gabungan)

# Content-Based Filtering

# In[48]:


cosine_sim_df = pd.DataFrame(cosine_sim_subset, 
                             index=apk_user_dict['App'], 
                             columns=apk_user_dict['App'])


# Collaborative Filtering

# In[49]:


item_similarity_df_train = pd.DataFrame(item_similarity_train, index=item_matrix_train.index, columns=item_matrix_train.index)


# Fungsi Prediksi Menggunakan Weighted Sum dengan Sentiment_Polarity

# In[51]:


def predict_polarity(app_name, user_ratings, similarity_matrix, n_neighbors=5):
    # Cari aplikasi yang mirip berdasarkan similarity matrix
    similar_apps = similarity_matrix[app_name].nlargest(n_neighbors + 1).index.drop(app_name, errors='ignore')
    
    # Ambil similarity scores dan Sentiment_Polarity dari aplikasi yang mirip
    sim_scores = similarity_matrix[app_name][similar_apps]
    app_polarity = user_ratings[similar_apps]
    
    # Menghitung weighted sum untuk prediksi Sentiment_Polarity
    weighted_sum = (sim_scores * app_polarity).sum()
    sim_sum = sim_scores.sum()
    
    # Jika sim_sum bukan nol, hitung rata-rata berbobot
    if sim_sum != 0:
        return weighted_sum / sim_sum
    else:
        return 0  # Jika tidak ada similarity, prediksi default


# Memprediksi Sentiment_Polarity untuk Item di Test Set

# In[52]:


# Inisialisasi daftar untuk menyimpan prediksi Sentiment_Polarity
y_pred_polarity = []

# Prediksi Sentiment_Polarity untuk setiap aplikasi dalam test set
for app in test_data['App']:
    try:
        # Prediksi Sentiment_Polarity menggunakan weighted sum
        pred_polarity = predict_polarity(app, train_data.pivot_table(index='App', values='Sentiment_Polarity'), item_similarity_df_train)
        y_pred_polarity.append(pred_polarity)
    except KeyError:
        # Jika aplikasi tidak ada dalam training set, beri prediksi default (misal 0)
        y_pred_polarity.append(0)

# Evaluasi hasil prediksi
mse_polarity = mean_squared_error(test_data['Sentiment_Polarity'], y_pred_polarity)
mae_polarity = mean_absolute_error(test_data['Sentiment_Polarity'], y_pred_polarity)

print(f"Mean Squared Error (Sentiment_Polarity): {mse_polarity}")
print(f"Mean Absolute Error (Sentiment_Polarity): {mae_polarity}")


# In[65]:


def hybrid_recommendations(app_name, content_sim_matrix, collab_sim_matrix, apk_user_dict, train_data, weight_content=0.5, weight_collab=0.5, n=10):
    # 1. Content-based Recommendations (based on 'genre')
    genre = apk_user_dict.loc[apk_user_dict['App'] == app_name, 'Category'].values[0]
    content_similar_apps = apk_user_dict[apk_user_dict['Category'] == genre]['App'].head(n+1).values
    content_similar_apps = [app for app in content_similar_apps if app != app_name]  # Exclude current app

    # 2. Collaborative-based Recommendations (based on 'Sentiment_Polarity')
    collab_similar_apps = collab_sim_matrix[app_name].nlargest(n + 1).index.drop(app_name, errors='ignore')

    # 3. Combine both recommendations
    combined_similar_apps = set(content_similar_apps).union(set(collab_similar_apps))

    # 4. Assign weights and calculate final scores
    final_scores = {}
    for app in combined_similar_apps:
        content_score = 1 if app in content_similar_apps else 0  # Genre match as binary score
        collab_score = collab_sim_matrix[app_name].get(app, 0)  # Sentiment polarity-based score

        # Combine with weights
        final_score = (weight_content * content_score) + (weight_collab * collab_score)
        final_scores[app] = final_score

    # 5. Sort results based on combined score
    sorted_apps = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)[:n]

    # 6. Fetch app details from apk_user_dict, excluding 'Translated_Review', 'Sentiment', and 'Category' columns
    recommended_apps = [app[0] for app in sorted_apps]
    recommendations = apk_user_dict[apk_user_dict['App'].isin(recommended_apps)].drop(columns=['Translated_Review', 'Sentiment', 'Category'])

    # 7. Sort final recommendations by 'Sentiment_Polarity'
    sorted_recommendations = recommendations.sort_values(by='Sentiment_Polarity', ascending=False).head(n)

    # 8. Format recommendations as a single row table
    single_row = sorted_recommendations.to_string(index=False, header=True)

    return single_row

# Contoh penggunaan
app_name_input = input("Masukkan nama aplikasi: ")
recommendations = hybrid_recommendations(app_name_input, cosine_sim_df, item_similarity_df_train, apk_user_dict, train_data, weight_content=0.5, weight_collab=0.5, n=10)
print(recommendations)

