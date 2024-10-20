import sqlite3
import csv
import uuid

# Set your CSV file path here
csv_file_path = 'dataset.csv'
db_file = 'db.sqlite3'
table_name = 'main_food'

# Connect to SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
# Create the table with a UUID as the PRIMARY KEY
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id TEXT PRIMARY KEY,
        nama_makanan_minuman TEXT,
        harga INTEGER,
        rating_ulasan REAL,
        nama_resto TEXT,
        alamat TEXT,
        kontak TEXT,
        waktu_buka_tutup TEXT,
        deskripsi TEXT
    )
''')

# Open the CSV file and read the data
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Skip header row

    # Insert each row with a UUID as the primary key
    for row in reader:
        row_id = str(uuid.uuid4())  # Generate a UUID for each row
        cursor.execute(f'''
            INSERT INTO {table_name} (
                id, nama_makanan_minuman, harga, rating_ulasan, nama_resto,
                alamat, kontak, waktu_buka_tutup, deskripsi
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row_id, *row))

# Commit changes and close connection
conn.commit()
conn.close()

print("Data imported successfully with UUIDs into the SQLite database!")
