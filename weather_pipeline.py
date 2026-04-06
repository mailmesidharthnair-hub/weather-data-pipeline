import requests
import psycopg2
import os
import logging
from datetime import datetime

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting weather data pipeline")

API_KEY = os.getenv("OPENWEATHER_API_KEY")

try:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    cursor = conn.cursor()
    logging.info("Database connection established")

except Exception as e:
    logging.error(f"Database connection failed: {e}")
    raise

try:
    with open("cities.txt", "r") as file:
        cities = file.read().splitlines()

    logging.info(f"{len(cities)} cities loaded from cities.txt")

except Exception as e:
    logging.error(f"Failed to read cities file: {e}")
    raise

for city in cities:

    try:
        logging.info(f"Fetching weather data for {city}")

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code != 200:
            logging.error(f"API request failed for {city}")
            continue

        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]

        timestamp = datetime.utcnow()

        cursor.execute(
            """
            INSERT INTO weather_data 
            (city, temperature, humidity, weather_description, timestamp)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (city, temperature, humidity, weather_desc, timestamp)
        )

        conn.commit()

        logging.info(f"Inserted weather data for {city}")

    except Exception as e:
        logging.error(f"Error processing {city}: {e}")

cursor.close()
conn.close()

logging.info("Weather data pipeline finished successfully")
