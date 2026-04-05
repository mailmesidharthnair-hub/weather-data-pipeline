import requests
import psycopg2
import logging
import os
from datetime import datetime

logging.basicConfig(
    filename="weather_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    CITY = ["Delhi", "Mumbai, "Bangalore", "Chennai"]

    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    city = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_desc = data["weather"][0]["description"]
    timestamp = datetime.now()

    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        sslmode="require"
    )

    cur = conn.cursor()

    cur.execute("""
        INSERT INTO weather_data (city, temperature, humidity, weather_description, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """, (city, temperature, humidity, weather_desc, timestamp))

    conn.commit()

    cur.close()
    conn.close()

    logging.info("Weather data inserted successfully")

except Exception as e:
    logging.error(f"Pipeline failed: {e}")
