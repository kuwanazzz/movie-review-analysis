import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("IMDB Dataset.csv")

# Eksplorasi awal
print(df.shape)       
print(df.columns)     
print(df.info())      
print(df.head())      
print(df['sentiment'].value_counts())

# Distribusi sentiment
sns.countplot(x="sentiment", data=df)
plt.title("Distribusi Sentiment Review Film")
plt.show()

# Analisis panjang review
df['review_length'] = df['review'].apply(lambda x: len(x.split()))

plt.figure(figsize=(8,5))
sns.histplot(data=df, x="review_length", bins=50, hue="sentiment", element="step")
plt.title("Distribusi Panjang Review berdasarkan Sentiment")
plt.xlabel("Jumlah Kata")
plt.ylabel("Jumlah Review")
plt.show()

# Statistik tambahan
print("Rata-rata panjang review per sentiment:")
print(df.groupby("sentiment")["review_length"].mean())

import mysql.connector
import pandas as pd

# Load dataset
df = pd.read_csv("IMDB Dataset.csv")

print("Jumlah data:", df.shape)  # cek dulu data masuk

# Koneksi ke MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",   # ganti password MySQL kamu
    database="imdb_reviews"
)
cursor = conn.cursor()

# Query insert
sql = "INSERT INTO reviews (review, sentiment) VALUES (%s, %s)"

# Convert dataframe ke list of tuples
data = list(df[['review', 'sentiment']].itertuples(index=False, name=None))

# Insert banyak sekaligus
cursor.executemany(sql, data)

# Commit perubahan
conn.commit()
print(cursor.rowcount, "baris berhasil dimasukkan.")

conn.close()


conn = mysql.connector.connect(
    host="localhost3306",
    user="root",
    password="kuwanaMSK132",
    database="imdb_reviews"
)
