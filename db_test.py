import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="weather_pipeline",
    user="postgres",
    password="020804"
)

cur = conn.cursor()

cur.execute("""
INSERT INTO weather_data (city, temperature, humidity, weather_description, timestamp)
VALUES ('Delhi', 30.5, 60, 'Clear sky', NOW())
""")

conn.commit()

cur.close()
conn.close()

print("Data inserted successfully!")