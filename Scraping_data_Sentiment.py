from google_play_scraper import reviews_all
import pandas as pd

def get_play_store_reviews(app_id, max_results):
    # Mengambil ulasan
    reviews = reviews_all(app_id, lang='id', country='id')
    reviews = reviews[:max_results]  # Batasi jumlah hasil
    return reviews

# ID aplikasi di Play Store
app_id = 'com.whatsapp'
reviews = get_play_store_reviews(app_id, 10000)  # Ambil hingga 10.000 ulasan

# Convert to DataFrame and save to CSV
df = pd.DataFrame(reviews)
df.to_csv('play_store_reviews.csv', index=False)